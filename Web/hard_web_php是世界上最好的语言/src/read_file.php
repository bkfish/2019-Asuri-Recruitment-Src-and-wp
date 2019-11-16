<?php
header("Content-type: text/html; charset=utf-8");
if(!isset($_GET['file']))
{
    if($_COOKIE['user'] === 'admin')
    {        
        echo "欢迎管理员,你可以在这里访问本站所有内容"."<br>";
        echo "本站有如下网页："."<br>";
        echo "index.php<br>";
        echo "read_file.php<br>";
        echo "no_flag_here.php<br>";
        echo "<br><br><br>";
    }
    else
    {
        die("emmm，本网站只供名为为admin的user访问");
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>readfile</title>
</head>
<body>
    <form method="GET">
        <input name="file" type="text"/>
        <input name="submit" type="button" value="提交"/>
    </form>
</body>
</html>
<?php
    if(isset($_GET['file']))
    {
        include_once($_GET['file']);
    }
?>

