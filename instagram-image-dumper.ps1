###############################
# Create by baurmatt@2013
# instagram-image-dumper.ps1
# Description: Script which downloads all images from Instagram for the specified user
###############################

$UserName = "alanarblanchard"
$DownloadPath = "D:\Downloads\-1- Instagram Test"

#############################################
# Nothing to change for you below this line #
#############################################

$JsonData = Invoke-WebRequest "http://instagram.com/$UserName/media" | ConvertFrom-Json
$UserDownloadPath = Join-Path -Path $DownloadPath -ChildPath $UserName

if(!(Test-Path $UserDownloadPath)){New-Item -ItemType Directory -Path $UserDownloadPath}

while($JsonData.more_available -eq $true){
    foreach($item in $JsonData.items){
        $ImageURL = $item.images.standard_resolution.url
        $ImageDownloadPath = Join-Path -Path $UserDownloadPath -ChildPath $ImageURL.Split('/')[-1]

        if(!(Test-Path $ImageDownloadPath)){
            Invoke-WebRequest $ImageURL -OutFile $ImageDownloadPath
        }
    }

    $LastID = ($JsonData.items | Select -Last 1).id
    $JsonData = Invoke-WebRequest "http://instagram.com/$UserName/media?max_id=$LastID" | ConvertFrom-Json
}