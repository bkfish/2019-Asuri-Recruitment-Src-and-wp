<?php
    header("Content-type: text/html; charset=utf-8");
    if(isset($_COOKIE['user']))
    {
        if($_COOKIE['user'] === 'admin')
        {        
            header('Refresh:3;url=read_file.php');
            echo "欢迎管理员";
        }
        else
        {
            die("emmm，本网站只供名为为admin的user访问");
        }
    }
    else
    {
        setcookie('user','guest',0,'/');
        die("emmm，本网站只供名为为admin的user访问");
    }
?>