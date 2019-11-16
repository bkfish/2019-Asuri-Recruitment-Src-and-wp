<!DOCTYPE html>
<html><head><meta charset="utf-8" />
<title>Hi hacker</title>
</head>
<body bgcolor="bisque">
<form action="index.php" method="get">用户名：<br><input type="text" name="name"><br>密码：<br><input type="text" name="password"><br><br><input type="submit" value="登陆">
</form>
<p>hint:admin用户的密码似乎在某个页面里 </p>
<p>
<?php
//error_reporting(0);

if( $_GET['name']&&$_GET['password']){
	if( $_GET['name']=='admin'&&$_GET['password']=='passwordbyyl'){
			echo '看你骨骼精奇，就将flag交于你了！';
			include('f111aaaaaaaaaggg.php');
	}
	else
		echo'账户或密码错误，请重新输入！';
}
else
	echo'请输入账户密码';



?>
</p>
</body>
</html>

