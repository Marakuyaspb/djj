<?php
/*
Template name: products
*/

get_header('new'); 
?>

<div id="goods_all"></div> 
<div id="goods_show" class ="products_container"></div> 
<div id='goods_details'></div>

<div id="spinner"></div> 
<div id="error"></div> 

<!-- CATEGORIES -->
<div class="container-fluid mt-2" id='goods_categories'>
	<div class='row'>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="k1r" onclick="filterProducts(event);">
			<div class='latte_wrap p-4'>
	  			<!-- a href='http://temp.decona.ru/category-k1r-system/' -->
	  				<div class ='pt-5'>
			  			<p class='major-text'>Модульные системы</h4>
			  			<p>Конфигурация под любое пространство
			  		</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Base-copy.png">
		  		</a>
	  		</div>
	  	</div>

	  	<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="corner" onclick="filterProducts(event);">
	  		<div class='latte_wrap p-4'>
				<!-- a href='http://temp.decona.ru/category-corner/' -->
					<div class ='pt-5'>
			  			<p class='major-text'>Угловые диваны</h4>
			  			<p>Конфигурация под любое пространство
			  		</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Naples-copy-1568x784.png">
				</a>
			</div>
		</div>
	  	
	</div>

	<div class='row '>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="strict">
			<div class='latte_wrap p-4'>
				<!-- a href='#' -->
					<div class ='pt-5 ps-5'>
			  			<p class='major-text'>Прямые диваны</h4>
			  			<p>Конфигурация под любое пространство
			  		</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Borneo-copy.png">
				</a>
			</div>
		</div>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="arm" onclick="filterProducts(event);">
			<div class='latte_wrap p-4'>
				<!-- a href='http://temp.decona.ru/category-armchair/' -->
					<div class ='pt-5 ps-5'>
			  			<p class='major-text'>Кресла</h4>
			  			<p>Конфигурация под любое пространство
			  		</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Brooklyn-copy.png">
				</a>
			</div>
		</div>
	</div>
	<div class='row'>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="bed" >
			<div class='latte_wrap p-4'>
				<!-- a href='#' -->
					<div class ='pt-5 ps-5'>
			  			<p class='major-text'>Кровати</h4>
			  			<p>Конфигурация под любое пространство
			  		</div>
					<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Beds-copy.png">
				</a>
			</div>
		</div>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="table">
			<div class='latte_wrap p-4'>
				<!-- a href='#' -->
					<div class ='pt-5 ps-5'>
			  			<p class='major-text'>Столы</h4>
			  			<p>Конфигурация под любое пространство
			  		</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Tables-copy.png">
				</a>
			</div>
		</div>
	</div>
	<div class='row'>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="pouf" onclick="filterProducts(event);">
			<div class='latte_wrap p-4'>
				<!-- a href='http://temp.decona.ru/category-pouf/' -->
					<div class ='pt-5 ps-5'>
			  			<p class='major-text'>Пуфы</h4>
			  			<p>Конфигурация под любое пространство
			  		</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Pouf-copy.png">
				</a>
			</div>
		</div>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="accessory" >
			<div class='latte_wrap p-4'>
				<!-- a href='#' -->
					<div class ='pt-5 ps-5'>
			  			<p class='major-text'>Аксессуары</h4>
			  			<p>Конфигурация под любое пространство
			  		</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Pod-copy.png">
				</a>
			</div>
		</div>
	</div>
</div>
 

<!-- GRAY RECTANGLES START -->

<!-- DESKTOP -->
<div class='container-fluid mb-5 d-none d-lg-block d-xl-block d-xxl-block' id='desctop-show'>
	<div class='row'>
		<div class ='col-md-4 rectangle latte_bg'> <!-- #F6F1EE -->
			<div class='bottom-align'>
				<h2 class='rect-card ps-4'>Каталог</h2>
				<h2 class='ps-4'>2023</h2>
				<a href='#' class='ms-4'><button class='btn-outline-gray'>Скачать каталог</button></a>
			</div>
		</div>
		<div class ='col-md-4 rectangle dark-gray'> <!-- #50504E -->
			<div class='bottom-align'>
				<h2 class='white rect-card ps-4'>Свяжитесь</h2>
				<h2 class='white ps-4'>с нами</h2>
				<a href='#' class='ms-4'><button class='btn-outline-white'>Обратная связь</button></a>
			</div>
		</div>
		<div class ='col-md-4 rectangle middle-gray ps-4'><!-- #CDCECF -->
			<div class='bottom-align'>
				<h2 class='rect-card ms-4'>Все акции и спецпредложения</h2>
				<a href='#' class='ms-4'><button class='btn-outline-gray'>Все акции</button></a>
			</div>
		</div>
	</div>
</div>

<!-- TABLET -->
<div class='container-fluid pt-5 d-none d-sm-block d-md-block d-lg-none' id='tablet-show'>
	<div class='row'>
		<div class ='col-md-4 rectangle latte_bg'> <!-- #F6F1EE -->
			<div class='bottom-align'>
				<h3 class='rect-card ps-4'>Каталог</h3>
				<h3 class='ps-4'>2023</h3>
				<a href='#' class='ms-4'><button class='btn-outline-gray'>Скачать каталог</button></a>
			</div>
		</div>
		<div class ='col-md-4 rectangle dark-gray'> <!-- #50504E -->
			<div class='bottom-align'>
				<h3 class='white rect-card ps-4'>Свяжитесь</h3>
				<h3 class='white ps-4'>с нами</h3>
				<a href='#' class='ms-4'><button class='btn-outline-white'>Обратная связь</button></a>
			</div>
		</div>
		<div class ='col-md-4 rectangle middle-gray ps-4'><!-- #CDCECF -->
			<div class='bottom-align'>
				<h3 class='rect-card ps-4'>Все акции и спецпредложения</h3>
				<a href='#' class='ms-4'><button class='btn-outline-gray'>Все акции</button></a>
			</div>
		</div>
	</div>
</div>

<!-- PHONE -->
<div class='container-fluid pt-5 d-block d-sm-none' id='phone-show'>
	<div class='row'>
		<div class ='col-md-4 rectangle latte_bg'> <!-- #F6F1EE -->
			<div class='bottom-align'>
				<h3 class='rect-card ps-2'>Каталог</h3>
				<h3 class='ps-2'>2023</h3>
				<a href='#' class='ms-2'><button class='btn-outline-gray'>Скачать каталог</button></a>
			</div>
		</div>
		<div class ='col-md-2 rectangle dark-gray'> <!-- #50504E -->
			<div class='bottom-align'>
				<h3 class='white rect-card ps-2'>Свяжитесь</h3>
				<h3 class='white ps-2'>с нами</h3>
				<a href='#' class='ms-2'><button class='btn-outline-white'>Обратная связь</button></a>
			</div>
		</div>
		<div class ='col-md-4 rectangle middle-gray ps-2'><!-- #CDCECF -->
			<div class='bottom-align'>
				<h3 class='rect-card ms-2'>Все акции и спецпредложения</h3>
				<a href='#' class='ms-2'><button class='btn-outline-gray'>Все акции</button></a>
			</div>
		</div>
	</div>
</div>
<!-- GRAY RECTANGLES END -->

<?php
get_footer();