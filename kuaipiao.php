<?php
    function main_handler($event,$time){



	//脚本设置
	
	$userID = '608b94a0fca746ab8938f1b28ef6867c';  //填写userID
	$sckey = 'SCU33968T48df213a4f6b5e35d3bf2856c938acd75bc00716e9d47'; //填写sever酱sckey
	$sign_msg = '1';   //签到通知选项,0是不通知,1是成功失败都通知,2是只有失败通知

	$sign_api = 'http://d.beichixing.xyz/cron/index/css';  //签名计算api,一般无需改动






	$headers = array(
	    "Referer: http://h5.kpcx179.com/kpcxAppOrther/appOrther/sign/signIn.html?userId=".$userID,
	    "Accept: text/html, application/xhtml+xml, image/jxr, */*",
	    "User-Agent: Mozilla/5.0 (Linux; Android 9; MI MAX 3 Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36; unicom{version:android@7.0000,desmobile:15690507717};devicetype{deviceBrand:Xiaomi,deviceModel:MI MAX 3}"
	        );
	//获取时间戳
	$timestamp = post('https://app.kpcx179.com/kpcx/appOrders/getSystemTime','',$headers);
	$time = json_decode($timestamp,true);
	$time = $time['Result']['systemTime'];
	$time = substr($time,0,strpos($time,':'));
	
	//计算签名
	$sign = get($sign_api.'?a={"userID":"'.$userID.'"}&b='.$time,$headers);

	//开始签到
	$result = post('https://app.kpcx179.com/integral/appsignin/saveSignIn','param={"userID":"'.$userID.'"}&sign='.$sign,$headers);
	$result = json_decode($result,true);

	if($result['Code'] == 0){
	$response = "签到成功,获得了".$result['Result']['score']."积分";
	if($sign_msg == '1'){
	get('https://sc.ftqq.com/'.$sckey.'.send?text='.urlencode($response));	
	}
	}else if($result['Code'] == 5){
	$response = "你今天已经签到过了";
	}else{
	$response = "签到失败,未知异常";
	if($sign_msg == '1'||$sign_msg == '2'){
	get('https://sc.ftqq.com/'.$sckey.'.send?text='.urlencode($response));	
	}
	}
	
	echo $response;
	
    }


    function post($url, $data,$headers) {

	   //初使化init方法
	   $ch = curl_init();
	   //指定URL
	   curl_setopt($ch, CURLOPT_URL, $url);
	   //设定请求后返回结果
	   curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	   //声明使用POST方式来进行发送
	   curl_setopt($ch, CURLOPT_POST, 1);
	   //发送什么数据呢
	   curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
	   //忽略证书
	   curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
	   curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
	   curl_setopt($ch, CURLOPT_HTTPHEADER,$headers);
	   //设置超时时间
	   curl_setopt($ch, CURLOPT_TIMEOUT, 10);
	   //发送请求
	   $output = curl_exec($ch);
	   //关闭curl
	   curl_close($ch);
	   //返回数据
	   return $output;
	}
	function get_location($url,$cookie,$headers) {

	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_COOKIE, $cookie);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
	curl_setopt($ch, CURLOPT_HTTPHEADER,$headers);
	// 不需要页面内容
	curl_setopt($ch, CURLOPT_NOBODY, 1);
	// 不直接输出
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	// 返回最后的Location
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
	curl_exec($ch);
	$info = curl_getinfo($ch,CURLINFO_EFFECTIVE_URL);
	curl_close($ch);
	   //返回数据
	   return $info;
	}
	function get($url,$headers) {

	   //初使化init方法
	   $ch = curl_init();
	   //指定URL
	   curl_setopt($ch, CURLOPT_URL, $url);
	   //设定请求后返回结果
	   curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	   //声明使用POST方式来进行发送
	   curl_setopt($ch, CURLOPT_POST, false);
	   //忽略证书
	   curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
	   curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
	   curl_setopt($ch, CURLOPT_HTTPHEADER,$headers);
	   //设置超时时间
	   curl_setopt($ch, CURLOPT_TIMEOUT, 10);
	   //发送请求
	   $output = curl_exec($ch);
	   //关闭curl
	   curl_close($ch);
	   //返回数据
	   return $output;
	}
?>

