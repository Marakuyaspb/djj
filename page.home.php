<?php
/*
Template name: home
*/

get_header(); 
?>

<!-- General slider start-->
	<!-- DESCTOP -->
	<div class='d-none d-md-block d-lg-block d-xl-block d-xxl-block' id='desctop-show'>
		<div class="main-head-slider">
			<div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
			  <div class="carousel-indicators">
			    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
			    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
			    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
			  </div>

			  <div class="carousel-inner">
			    <div class="carousel-item active">
			      <img src="http://temp.decona.ru/wp-content/uploads/2023/03/Untitled-4-1.png" class="d-block w-100" alt="...">
			    </div>
			    <div class="carousel-item">
			      <img src="http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_INTERIORS/CONSONO_1.jpg" class="d-block w-100" alt="...">
			    </div>
			    <div class="carousel-item">
			      <img src="http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_INTERIORS/CONSONO_3.jpg" class="d-block w-100" alt="...">
			    </div>
			  </div>
			  
			  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
			    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
			    <span class="visually-hidden">Previous</span>
			  </button>
			  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
			    <span class="carousel-control-next-icon" aria-hidden="true"></span>
			    <span class="visually-hidden">Next</span>
			  </button>
			</div>

			<div class="ps-5 over-slider">
				<h1 class="white slider_h1">BASE</h1>
				<p class="white ms-2 mb-5 major-text just-thin">Модульная система</p>
				<a href='http://temp.decona.ru/2023/04/18/great-offer/' class='ms-2 pb-3'><button class='btn-outline-white-main-slider'>Подробнее</button></a>
			</div>
		</div>
	</div>

	<!-- TABLET & PHONE -->
	<div class='pt-5 d-block d-md-none ' id='phone-show'>
		<div class="main-head-slider">
			<div id="carouselExampleIndicators" class="carousel slide mb-5" data-bs-ride="carousel">
			  <div class="carousel-indicators">
			    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
			    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
			    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
			    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
			  </div>
			  <div class="carousel-inner">
			    <div class="carousel-item active">
			      <img src="http://temp.decona.ru/wp-content/uploads/2023/03/verticall_1.png" class="d-block w-100" alt="...">
			    </div>
			    <div class="carousel-item">
			      <img src="http://temp.decona.ru/wp-content/uploads/2023/03/verticall_0.png" alt="...">
			    </div>
			    <div class="carousel-item">
			      <img src="http://temp.decona.ru/wp-content/uploads/2023/03/verticall_2.png" class="d-block w-100" alt="...">
			    </div>
			    <div class="carousel-item">
			      <img src="http://temp.decona.ru/wp-content/uploads/2023/03/verticall_3.png" class="d-block w-100" alt="...">
			    </div>
			  </div>
			  
			</div>

			<div class="over-slider-mobile">
				<h2 class="white ps-2">BASE</h2>
				<p class="white just-thin ps-2 ms-2 mb-4">Модульная система</p>
				<a href='http://temp.decona.ru/products/' class='ms-2 ps-2 pb-3'><button class='btn-outline-white'>Подробнее</button></a>
			</div>
		</div>
	</div>
<!-- General slider end -->

	<div id="goods_all"></div> 
	<div id="goods_show" class ="products_container"></div> 
	<div id='goods_details'></div>

	<div id="spinner"></div> 
	<div id="error"></div> 

<!-- slider finish -->


<!-- CATEGORIES DESCTOP-->
<div class='container-fluid mt-2 d-none d-md-block d-lg-block d-xl-block d-xxl-block' id='goods_categories_desctop'>
	<div class='row'>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="k1r" onclick="filterProducts(event);">
			<div class='latte_wrap my-2 p-4'>
	  			<!-- a href='http://temp.decona.ru/category-k1r-system/' -->
	  				<div class ='category_label'>
			  			<p class='major-text'>Модульные системы</p>
			  			<p class='small-text'>Конфигурация под любое пространство
			  		</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Base-copy.png">
		  		</a>
	  		</div>
	  	</div>
	  	<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="corner" onclick="filterProducts(event);">
	  		<div class='latte_wrap my-2  p-4'>
				<!-- a href='http://temp.decona.ru/category-corner/' -->
					<div class ='category_label'>
			  			<p class='major-text'>Угловые диваны</p>
			  			<p class='small-text'>Стиль и трансформация
			  		</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Naples-copy-1568x784.png">
				</a>
			</div>
		</div> 	
	</div>

	<div class='row '>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="sofa" onclick="filterProducts(event);">
			<div class='latte_wrap my-2 p-4'>
				<!-- a href='#' -->
					<div class ='category_label'>
			  			<p class='major-text'>Прямые диваны</p>
			  			<p class='small-text'>Классика мягкой мебели
			  		</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Borneo-copy.png">
				</a>
			</div>
		</div>

		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="arm" onclick="filterProducts(event);">
			<div class='latte_wrap my-2 p-4'>
				<!-- a href='http://temp.decona.ru/category-armchair/' -->
					<div class ='category_label'>
			  			<p class='major-text'>Кресла</p>
			  			<p class='small-text'>Для гостиной и лаундж-зоны
			  		</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Brooklyn-copy.png">
				</a>
			</div>
		</div>
	</div>

	<div class='row'>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="bed" onclick="filterProducts(event);">
			<div class='latte_wrap my-2 p-4'>
				<!-- a href='#' -->
					<div class ='category_label'>
			  			<p class='major-text'>Кровати</p>
			  			<p class='small-text'>Восстановление сил
			  		</div>
					<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Beds-copy.png">
				</a>
			</div>
		</div>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="table">
			<div class='latte_wrap my-2 p-4'>
				<!-- a href='#' -->
					<div class ='category_label'>
			  			<p class='major-text'>Столы</p>
			  			<p class='small-text'>Надежность и стиль
			  		</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Tables-copy.png">
				</a>
			</div>
		</div>
	</div>
	<div class='row'>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="pouf" onclick="filterProducts(event);">
			<div class='latte_wrap my-2 p-4'>
				<!-- a href='http://temp.decona.ru/category-pouf/' -->
					<div class ='category_label'>
			  			<p class='major-text'>Пуфы</p>
			  			<p class='small-text'>Большие и маленькие
			  		</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Pouf-copy.png">
				</a>
			</div>
		</div>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="accessory" >
			<div class='latte_wrap my-2 p-4'>
				<!-- a href='#' -->
					<div class ='category_label'>
			  			<p class='major-text'>Аксессуары</p>
			  			<p class='small-text'>Финальные штрихи к интерьеру
			  		</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Pod-copy.png">
				</a>
			</div>
		</div>
	</div>
</div>

<!-- CATEGORIES PHONE & TABLET-->
<div class='container-fluid mt-5 d-block d-md-none' id='goods_categories_phone'>
	<div class='row'>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="k1r" onclick="filterProducts(event);">
			<div class='latte_wrap p-1'>
	  			<div class ='pt-2'>
			  		<p class='major-text just-thin'>Модульные системы</h4>
			  	</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Base-copy.png">
	  		</div>
	  	</div>

	  	<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="corner" onclick="filterProducts(event);">
	  		<div class='latte_wrap p-1'>
				<div class ='pt-2'>
			  		<p class='major-text just-thin'>Угловые диваны</h4>
				</div>
	  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Naples-copy-1568x784.png">
			</div>
		</div>
	  	
	</div>

	<div class='row '>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="sofa" onclick="filterProducts(event);">
			<div class='latte_wrap p-1'>
				<div class ='pt-2'>
		  			<p class='major-text just-thin'>Прямые диваны</h4>	
		  		</div>
  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Borneo-copy.png">
			</div>
		</div>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="arm" onclick="filterProducts(event);">
			<div class='latte_wrap p-1'>
				<div class ='pt-2'>
		  			<p class='major-text just-thin'>Кресла</h4>
		  		</div>
  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Brooklyn-copy.png">
			</div>
		</div>
	</div>
	<div class='row'>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="bed" onclick="filterProducts(event);">
			<div class='latte_wrap p-1'>
				<div class ='pt-2'>
		  			<p class='major-text just-thin'>Кровати</h4>
		  			
		  		</div>
				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Beds-copy.png">
			</div>
		</div>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="table">
			<div class='latte_wrap p-1'>
				<div class ='pt-2'>
		  			<p class='major-text just-thin'>Столы</h4>
		  			
		  		</div>
  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Tables-copy.png">
			</div>
		</div>
	</div>
	<div class='row'>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="pouf" onclick="filterProducts(event);">
			<div class='latte_wrap p-1'>
				<div class ='pt-2'>
		  			<p class='major-text just-thin'>Пуфы</h4>
		  		</div>
  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Pouf-copy.png">
			</div>
		</div>
		<div class="col-md-6 col-sm-12 py-1 row_prod_catgories" id="accessory" >
			<div class='latte_wrap p-1'>
				<div class ='pt-2'>
		  			<p class='major-text just-thin'>Аксессуары</h4>	
		  		</div>
  				<img class='img-fluid card-product-category'  src="http://temp.decona.ru/wp-content/uploads/2023/03/Prod_Pod-copy.png">
			</div>
		</div>
	</div>
</div>


<!-- GRAY RECTANGLES START -->
	<!-- DESKTOP -->
	<div class='my-5 mx-4 d-none d-lg-block d-xl-block d-xxl-block' id='desctop-show'>
		<div class='d-flex justify-content-between'>
			<div class ='rectangle latte_bg ps-4'> <!-- #F6F1EE -->
				<h2 class='rect-card ps-4'>Каталог</h2>
				<h2 class='ps-4 mb-5'>2023</h2>
				<a href='http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_DOWNLOADS/PDF/CONSONO.pdf' class='ps-4'><button class='btn-outline-gray'>Скачать каталог</button></a>	
			</div>
			<div class ='rectangle dark-gray ps-4'> <!-- #50504E -->
				<h2 class='white rect-card ps-4'>Покупка в рассрочку </h2>
				<h2 class='white ps-4  mb-5'>без первого взноса</h2>
				<a href='http://temp.decona.ru/contact/' class='ps-4'><button class='btn-outline-white'>Обратная связь</button></a>
			</div>
			<div class ='rectangle middle-gray ps-4'><!-- #CDCECF -->
					<h2 class='rect-card ms-4'>Все акции</h2>
					<h2 class='ms-4 mb-5'>и спецпредложения</h2>
					<a href='http://temp.decona.ru/2023/04/18/great-offer/' class='ps-4'><button class='btn-outline-gray'>Все акции</button></a>
			</div>
			</div>

	</div>

	<!-- TABLET -->
	<div class='container-fluid pt-5 d-none d-sm-block d-md-block d-lg-none' id='tablet-show'>
		<div class='row'>
			<div class ='col-md-4 rectangle_mob latte_bg'> <!-- #F6F1EE -->
				<div class='bottom-align'>
					<h4 class='rect-card ps-2'>Каталог с новинками 2023 года</h4>
					<a href='#' class='ps-2'><button class='btn-outline-gray'>Скачать каталог</button></a>
				</div>
			</div>
			<div class ='col-md-4 rectangle_mob dark-gray'> <!-- #50504E -->
				<div class='bottom-align'>
					<h4 class='white rect-card ps-4'>Покупка в рассрочку без первого взноса</h4>
					<a href='#' class='ps-2'><button class='btn-outline-white'>Обратная связь</button></a>
				</div>
			</div>
			<div class ='col-md-4 rectangle_mob middle-gray ps-4'><!-- #CDCECF -->
				<div class='bottom-align'>
					<h4 class='rect-card ps-2'>Все акции и спецпредложения</h4>
					<a href='#' class='ps-2'><button class='btn-outline-gray'>Все акции</button></a>
				</div>
			</div>
		</div>
	</div>

	<!-- PHONE -->
	<div class='container-fluid pt-5 d-block d-sm-none' id='phone-show'>
		<div class='row'>
			<div class ='col-md-4 rectangle_mob latte_bg'> <!-- #F6F1EE -->
				<div class='bottom-align'>
					<h3 class='rect-card ps-2'>Каталог</h3>
					<h3 class='ps-2'>2023</h3>
					<a href='#' class='ms-2'><button class='btn-outline-gray'>Скачать каталог</button></a>
				</div>
			</div>
			<div class ='col-md-2 rectangle_mob dark-gray'> <!-- #50504E -->
				<div class='bottom-align'>
					<h3 class='white rect-card ps-2'>Свяжитесь</h3>
					<h3 class='white ps-2'>с нами</h3>
					<a href='#' class='ms-2'><button class='btn-outline-white'>Обратная связь</button></a>
				</div>
			</div>
			<div class ='col-md-4 rectangle_mob middle-gray ps-2'><!-- #CDCECF -->
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