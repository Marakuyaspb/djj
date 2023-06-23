<?php
/*
Template name: contact
*/

get_header('new'); 
?>

<div class="container container-fluid my-5">
	<div class='row'>
		<div class="col-md-6 col-sm-12">
			<h2 class="mb-5">Контакты фабрики</h2>

			<p>Россия, 192102, Санкт-Петербург, улица Самойловой, 5
			<p>Часы работы: 10.00 - 18.00
			<p>Телефон офиса: 8 (800) 500 13 72
			<p>E-mail: info@temp.decona.ru
		</div>
		<div class="col-md-6 col-sm-12 ymaps-layers-pane">
			<script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3A63e78d65fdf8fafa5fc0a64b5ee460a2d4962efdadb169890d1753e84524c2ad&amp;width=1015&amp;height=551&amp;lang=ru_RU&amp;scroll=true"></script>
		</div>
	</div>
</div>

<?php
get_footer();