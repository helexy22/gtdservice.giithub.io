<!DocumentType HTML>
<html>
<head>
<meta charset="urf-8">
<title>网址导航页的实现</title>
<link rel="stylesheet"type="text/css"href="css/base.css">
<style>
<!--页面整体的CSS规范-->
header{
    width:100px;
    height:200px;
    margin:40px auto;
}
<!--页面4个区块的CSS规则-->
.block{
    width:151px;
    height:90px;
    border-right:1px solid #ccc;
    margin-left:30px;
    margin-top:30px;
    float:left;
}
<!--列表中各项的CSS规则-->
.block ul li{
    width:50px;
    height:30px;
    text-align:left;
    float:left;
}
<!--超链接初始状态的样式-->
.block ul li a{
    color:#333;
    font-family:"微软雅黑"；
    font-size:12px;
    line-height:30px;
}
<!--鼠标悬停时的字体样式-->
.block ul li a:hover{
    color:#E66100;
    font-weight:bold;
}
</style>
</head>

<body>
<head>
    <nav>
<!--定义第一区块的HTML结构-->
    <div class="block">
        <ul>
            <li><a href="http://news.qq.com">腾讯</a></li>
            <li><a href="http://news.qq.com">网易</a></li>

        </ul>
        </div>
<!--定义第二区块的HTML结构-->
<div class="block">
        <ul>
            <li><a href="http://news.qq.com">腾讯</a></li>
            <li><a href="http://news.qq.com">网易</a></li>

        </ul>
        </div>
    </nav>
</header>    
</body>
</html>
