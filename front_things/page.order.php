<?php
/*
Template name: order
*/

get_header('new'); 
?>


<div class ='container-fluid'>
  <h1 class = 'sku' id = 'porland_HipHop'>Итак</h1>
	<h3>Оформить заказ</h3>
	<form action="http://temp.decona.ru/wp-content/uploads/mail_craft/mail.php" method="POST">
    	<p>Модель: 
    	<p class ='major-text' id="ordered_sku" name="user_sku"></p>
		<input type="text" name="user_name" placeholder ="Ваше имя" required>
		<select name="user_city">
			<option>Санкт-Петербург</option>
			<option>Москва</option>
			<option>Владикавказ</option>
			<option>Калининград</option>
			<option>Краснодаp</option>
			<option>Мурманск</option>
			<option>Нальчик</option>
			<option>Нижневартовск</option>
			<option>Псков</option>
			<option>Пятигорск</option>
			<option>Ставрополь</option>
		</select>
		<br>
		<input type="text" name="user_phone" placeholder ="Телефон" required>
		<input type="text" name="user_email" placeholder ="E-mail" required>
		<br>
		<button type="submit" class='btn-prod-card y-2'>Заказать</button>
	</form>
</div>

<script>
function pushSKUinForm(){
	let element = document.getElementsByClassName("sku");
	class_sku = element[0];
	let product_sku = class_sku.getAttribute('id');
	console.log(product_sku);
	document.getElementById('ordered_sku').innerHTML = `${product_sku}`;
};
pushSKUinForm();
</script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>