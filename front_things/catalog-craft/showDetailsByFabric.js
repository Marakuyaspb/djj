/* Change it! */
function showDetailsByFabric(event){
	
/* get SKU of product by the CLICK */
 	const clickedElement = event.currentTarget;
  	const currentSKU = clickedElement.id;
  	//console.log(`Clicked element ID: ${currentSKU}`);

/* compare the clicked SKU with all SKUs in [] */
   	for (let i = 0; i < CATALOG.length; ++i) {
	  	if (CATALOG[i].sku == currentSKU){

/*remove current html */
  			var currProduct = document.getElementById('goods_details');
  			currProduct.remove();

/* create a new var with all info about the match sku */
  			let productAllDetails = CATALOG[i];
  			//console.log(productAllDetails);

 /* define vars */
  			let sku = productAllDetails.sku;
  			let model = productAllDetails.model;
  			let collection = productAllDetails.collection;
  			let category = productAllDetails.category;
  			let category_ru = productAllDetails.category_ru;
  			let fabric_type = productAllDetails.fabric_type;
  			let fabric_name = productAllDetails.fabric_name;
  			let product_name = productAllDetails.product_name;
  			let product_img = productAllDetails.product_img;
  			let product_img_mob = productAllDetails.product_img_mob;
  			let is_new = productAllDetails.is_new;
  			let available_for_delivery_2 = productAllDetails.available_for_delivery_2;
  			let available_for_delivery_28 = productAllDetails.available_for_delivery_28;
  			let available_in_showroom = productAllDetails.available_in_showroom;
  			let carousel_item_1 = productAllDetails.carousel_item_1;
  			let carousel_item_2 = productAllDetails.carousel_item_2;
  			let carousel_item_3 = productAllDetails.carousel_item_3;
  			let carousel_item_4 = productAllDetails.carousel_item_4;
  			let carousel_item_5 = productAllDetails.carousel_item_5;
  			let carousel_item_1_mob = productAllDetails.carousel_item_1_mob;
  			let carousel_item_2_mob = productAllDetails.carousel_item_2_mob;
  			let carousel_item_3_mob = productAllDetails.carousel_item_3_mob;
  			let carousel_item_4_mob = productAllDetails.carousel_item_4_mob;
  			let carousel_item_5_mob = productAllDetails.carousel_item_5_mob;
  			let right_sofa_piece = productAllDetails.right_sofa_piece;
  			let product_full_name = productAllDetails.product_full_name;
  			let price = productAllDetails.price;
  			let price_sale = productAllDetails.price_sale;
  			let description = productAllDetails.description;
  			let prod_width = productAllDetails.prod_width;
  			let prod_depth = productAllDetails.prod_depth;
  			let prod_height = productAllDetails.prod_height;
  			let prod_weight = productAllDetails.prod_weight;
  			let prod_seat_height = productAllDetails.prod_seat_height;
  			let prod_seat_width = productAllDetails.prod_seat_width;
  			let prod_seat_depth = productAllDetails.prod_seat_depth;
  			let prod_back_width = productAllDetails.prod_back_width;
  			let product_type = productAllDetails.product_type;
  			let transform_type = productAllDetails.transform_type;
  			let matress_type = productAllDetails.matress_type;
  			let product_form = productAllDetails.product_form;
  			let product_style = productAllDetails.product_style;
  			let product_inside = productAllDetails.product_inside;
  			let features = productAllDetails.features;
  			let product_fabric_about = productAllDetails.product_fabric_about;
  			let product_fabric_img = productAllDetails.product_fabric_img;
  			let scheme = productAllDetails.scheme;
  			let scheme_2 = productAllDetails.scheme_2;
  			let paws_var = productAllDetails.paws_var;
  			let slider_interior_1 = productAllDetails.slider_interior_1;
  			let slider_interior_2 = productAllDetails.slider_interior_2;
  			let slider_interior_3 = productAllDetails.slider_interior_3;
  			let slider_interior_4 = productAllDetails.slider_interior_4;
  			let slider_interior_mob_1 = productAllDetails.slider_interior_mob_1;
  			let slider_interior_mob_2 = productAllDetails.slider_interior_mob_2;
  			let slider_interior_mob_3 = productAllDetails.slider_interior_mob_3;
  			let slider_interior_mob_4 = productAllDetails.slider_interior_mob_4;
			let canvas_background = productAllDetails.canvas_background;

/* render new html about the single product */
  		let anotherProduct = document.createElement("div");
  		anotherProduct.id = 'goods_details';
  		let placeHere = document.getElementById('spinner');
		placeHere.append(anotherProduct);
		document.getElementById('goods_details').innerHTML =
			`
<div id='${sku}' class='sku'>

	<!-- DESCTOP -->
	<div class='d-none d-md-block d-lg-block d-xl-block d-xxl-block'>

		<div class='thin ms-4'>
			<a id='collection' class='${collection}' href='http://temp.decona.ru/'>Продукция</a> / ${category_ru}
		</div>

		<div class='row'>
			<div class='${category}' id='content_left'>
				<p class='h-center'>${product_name}</p>
				<center>
		      	<p class='fabric-name pb-3'>Ткань: ${fabric_name}
		    	</center>

			<!-- fabric buttons -->

				<div class='slide-fabric-nav' onClick ='event.stopPropagation()'>  	  
					<img class='slide-fabric-button fabric-var-desctop fabric-var CAMBRIDGE_600' id='${collection}_${category}_CAMBRIDGE_600' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/CAMBRIDGE/ICONS/CAMBRIDGE_600.png' onClick ='showDetailsByFabric(event);'>

					<img class='slide-fabric-button fabric-var-desctop fabric-var COSMIC_08' id='${collection}_${category}_COSMIC_08' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/COSMIC/COSMIC_08.png' onClick ='showDetailsByFabric(event);'>

					<img class='slide-fabric-button fabric-var-desctop fabric-var HARMONY_SILVER' id='${collection}_${category}_HARMONY_SILVER' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/HARMONY/HARMONY_SILVER.png' onClick ='showDetailsByFabric(event);'>  

			    	<img class='slide-fabric-button fabric-var-desctop fabric-var JAZZ_01' id='${collection}_${category}_JAZZ_01' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/JAZZ/ICONS/JAZZ_01.png' onClick ='showDetailsByFabric(event);'>

			    	<img class='slide-fabric-button fabric-var-desctop fabric-var JAZZ_08' id='${collection}_${category}_JAZZ_08' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/JAZZ/ICONS/JAZZ_08.png' onClick ='showDetailsByFabric(event);'>

			    	<img class='slide-fabric-button fabric-var-desctop fabric-var JAZZ_21' id='${collection}_${category}_JAZZ_21' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/JAZZ/ICONS/JAZZ_21.png' onClick ='showDetailsByFabric(event);'>

			    	<img class='slide-fabric-button fabric-var-desctop fabric-var PIXEL_FOREST' id='${collection}_${category}_PIXEL_FOREST' src= 'http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/PIXEL/ICONS/PIXEL_FOREST.png' onClick ='showDetailsByFabric(event);'>
			    
			    	<img class='slide-fabric-button fabric-var-desctop fabric-var VELUTTO_16' id='${collection}_${category}_VELUTTO_16' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/VELUTTO/ICONS/VELUTTO_16.png' onClick ='showDetailsByFabric(event);'> 
				</div>

				<div class='d-flex flex-row ms-4 card_icons'>
					<img class = 'is_new_icon_pr_card' src='${is_new}'>
					<img class = 'available_icon_pr_card' src='${available_in_showroom}'> 
					<img class = 'available_icon_pr_card'src='${available_for_delivery_2}'>
				</div>

				<!-- slider with product -->

				<div id='carouselExampleDark' class='carousel carousel-dark slide' data-bs-ride='carousel'>
					<div class='carousel-indicators'>
					    <button type='button' data-bs-target='#carouselExampleDark' data-bs-slide-to='0' class='active' aria-current='true' aria-label='Slide 1'></button>
					    <button type='button' data-bs-target='#carouselExampleDark' data-bs-slide-to='1' aria-label='Slide 2'></button>
					    <button type='button' data-bs-target='#carouselExampleDark' data-bs-slide-to='2' aria-label='Slide 3'></button>
					    <button type='button' data-bs-target='#carouselExampleDark' data-bs-slide-to='3' aria-label='Slide 4'></button>
					    <button type='button' data-bs-target='#carouselExampleDark' data-bs-slide-to='4' aria-label='Slide 5'></button>
					</div>
					<div class='carousel-inner'>
					    <div class='carousel-item active' data-bs-interval='10000'>
					      <img src='${carousel_item_1}' class='d-block w-100' alt='...'>
					    </div>
					    <div class='carousel-item' data-bs-interval='2000'>
					      <img src='${carousel_item_2}' class='d-block w-100' alt='...'>
					    </div>
					    <div class='carousel-item'>
					      <img src='${carousel_item_3}' class='d-block w-100' alt='...'>
					    </div>
					    <div class='carousel-item'>
					      <img src='${carousel_item_4}' class='d-block w-100' alt='...'>
					    </div>
					    <div class='carousel-item'>
					      <img src='${carousel_item_5}' class='d-block w-100' alt='...'>
					    </div>
					</div>

					  <button class='carousel-control-prev' type='button' data-bs-target='#carouselExampleDark' data-bs-slide='prev'>
					    <span class='carousel-control-prev-icon' aria-hidden='true'></span>
					    <span class='visually-hidden'>Previous</span>
					  </button>
					  <button class='carousel-control-next' type='button' data-bs-target='#carouselExampleDark' data-bs-slide='next'>
					    <span class='carousel-control-next-icon' aria-hidden='true'></span>
					    <span class='visually-hidden'>Next</span>
					  </button>
				</div>  
			</div>

			<div class='no-padding-right' id='content_right'>
				<img class='img-fluid banner' src='${right_sofa_piece}'>
			</div>
		</div>



		<!-- Name & price -->
	
		<div class='d-flex justify-content-evenly latte_bg banner'>
			<div class='mt-2 prod-card-model'>
				${product_full_name}
			</div>
			<div class='mt-1 d-flex flex-row'>
				<p class='prod-card-price pe-3'>${price_sale} ₽</p>
				<p class='old-price'>${price} ₽</p>
			</div>
			<div class='mt-3 d-flex justify-content-between'>
				<a class='rel_pos' href='#'>
					<button class='to-order white btn-prod-card' onClick='pushSKUinForm(event);'>
						Заказать
					</button>
				</a>
				<a class='white rel_pos' href='http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_DOWNLOADS/3D/CONSONO_mods.zip'>
					<button class='white btn-prod-card'>
						3d модель
					</button>
				</a>
				<a class='white rel_pos' href='http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_DOWNLOADS/PDF/CONSONO.pdf'>
					<button class='white btn-prod-card'>
						PDF
					</button>
				</a>
			</div>
		</div>

		<!-- ACCORDION DESCTOP-->

		<div class='accordion mx-5' id='accordionExample'>
		    <div class='accordion-item'><!-- Описание -->
		        <h2 class='accordion-header' id='headingOne'>
		            <button class='accordion-button white_bg' type='button' data-bs-toggle='collapse' data-bs-target='#collapseOne' aria-expanded='true' aria-controls='collapseOne'>
		            Описание
		            </button>
		        </h2>
		        <div id='collapseOne' class='accordion-collapse collapse show' aria-labelledby='headingOne' data-bs-parent='#accordionExample'>
		            <div class='accordion-body'>
		                <p id='description'>
		                	${description}
		                </p>
		          	</div>
		        </div>
		    </div>

		    <div class='accordion-item'><!-- Схема и габариты -->
		        <h2 class='accordion-header' id='headingTwo'>
		            <button class='accordion-button' type='button' data-bs-toggle='collapse' data-bs-target='#collapseTwo' aria-expanded='true' aria-controls='collapseTwo'>
		            Схема и габариты
		            </button>
		        </h2>
		        <div id='collapseTwo' class='accordion-collapse collapse' aria-labelledby='headingTwo' data-bs-parent='#accordionExample'>
		            <div class='accordion-body'>
		            	<div class='container-fluid'>
							<div class='row'>
								<div class='col-md-4 col-sm-12'>
			                		<table class='prod-card-table'>
				                		<tr class='prod-card-table-row'>
											${prod_width}
										</tr>
										<tr class='prod-card-table-row'>
											${prod_depth}
										</tr>
										<tr class='prod-card-table-row'>
											${prod_height}
										</tr>
										<tr class='prod-card-table-row'>
											${prod_weight}
										</tr>
										<tr class='prod-card-table-row'>
											${prod_seat_height}
										</tr>
										<tr class='prod-card-table-row'>
											${prod_seat_width}
										</tr>
										<tr class='prod-card-table-row'>
											${prod_seat_depth}
										</tr>
										<tr class='prod-card-table-row'>
											${prod_back_width}
										</tr>
									</table>
									</table>

									<!-- button class='btn-outline-gray mt-1'>Вся коллекция</button -->

								</div>
								<div class='col-md-4 col-sm-12'>
									${scheme}
									${scheme_2}
								</div>
								
							</div>
						</div>
					</div>		
		          </div>
		    </div>
		    
		    <div class='accordion-item'><!-- Характеристики -->
		        <h2 class='accordion-header' id='headingThree'>
		            <button class='accordion-button' type='button' data-bs-toggle='collapse' data-bs-target='#collapseThree' aria-expanded='true' aria-controls='collapseThree'>
		            Характеристики
		            </button>
		        </h2>
		        <div id='collapseThree' class='accordion-collapse collapse' aria-labelledby='headingThree' data-bs-parent='#accordionExample'>
		            <div class='accordion-body'>
		                <h4>Основные</h4>
		                <div class='accordion-padding'>
							<div class='row'>
								<div class='col-md-6 col-sm-12'>
									<table class='prod-card-table'>
										<tr>
											${product_type}
										</tr>
										<tr>
											${transform_type}
										</tr>
										<tr>
											${matress_type}
										</tr>
									</table>
								</div>
								<div class='col-md-6 col-sm-12'>
									<table class='prod-card-table'>
										<tr>
											${product_form}
										</tr>
										<tr>
											${product_style}
										</tr>
										<tr>
											${product_inside}
										</tr>
									</table>
								</div>
								<p class='pt-3'>Конструктивные особенности: ${features}
							</div>
						</div>
		        	</div>
		    	</div>
		    </div>

		    <div class='accordion-item'><!-- Материал обивки -->
		        <h2 class='accordion-header' id='headingFour'>
		            <button class='accordion-button' type='button' data-bs-toggle='collapse' data-bs-target='#collapseFour' aria-expanded='true' aria-controls='collapseFour'>
		            Материал обивки
		            </button>
		        </h2>
		        <div id='collapseFour' class='accordion-collapse collapse' aria-labelledby='headingFour' data-bs-parent='#accordionExample'>
		            <div class='accordion-body'>
		            	<div class='container-fluid'>
							<div class='row'>
								<div class='col-md-8 col-sm-12'>
									<p>${product_fabric_about}
									<p>Обращаем Ваше внимание, что реальный цвет ткани может значительно отличаться от изображения на экране. Это зависит от индивидуальных настроек монитора и восприятия цвета. Поэтому при заказе ткани ориентируйтесь на реальные образцы.
		                			<p class='pt-2'>Больше образцов тканей вы можете посмотреть в наших салонах.
									<p><a href='http://temp.decona.ru/showrooms/'><button class='btn-outline-gray mt-3'>Адреса салонов</button></a>
								</div>
								<div class='col-md-4 col-sm-12'>
									<img src='${product_fabric_img}' class='img-fluid'>
								</div>
							</div>	
			          	</div>
			        </div>
			    </div>
			</div>

		    <div class='accordion-item'><!-- Варианты исполнения ножек -->
		        ${paws_var}
			</div>
	  
		    <div class='accordion-item'><!-- Опции -->
		        <h2 class='accordion-header' id='headingSix'>
		            <button class='accordion-button' type='button' data-bs-toggle='collapse' data-bs-target='#collapseSix' aria-expanded='true' aria-controls='collapseSix'>
		            Опции
		            </button>
		        </h2>
		        <div id='collapseSix' class='accordion-collapse collapse' aria-labelledby='headingSix' data-bs-parent='#accordionExample'>
		            <div class='accordion-body'>
		            	<div>
		                	<p class='mb-2'>Вы можете заказать диван как с декоративной отстрочкой внешних швов, так и без неё.
		                	</p>
		                </div>
		                <div class='container-fluid'>
		                	<div class='row'>
								<div class='ps-5 col-md-6 col-sm-12'>
									<p>Декоративные швы снаружи
									<img src='http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_OPTIONS/SEAMS/CONSONO_SEAMS.jpg'>
								</div>
								<div class='pe-5 col-md-6 col-sm-12'>
									<p>Без декоративных швов
									<img src='wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_OPTIONS/SEAMS/CONSONO_NOSEAMS.jpg'>
								</div>
							</div>
						</div>
		          	</div>
		        </div>
		    </div>
		</div>

		<!-- Slider with interiors DESCTOP -->
		<div class='banner mt-3'>
			<div id='carouselExampleIndicators' class='carousel slide' data-bs-ride='carousel'>
				<div class='carousel-indicators'>
				    <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='0' class='active' aria-current='true' aria-label='Slide 1'></button>
				    <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='1' aria-label='Slide 2'></button>
				    <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='2' aria-label='Slide 3'></button>
				    <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='3' aria-label='Slide 4'></button>
				</div>

				<div class='carousel-inner'>
				    <div class='carousel-item active'>
				      <img src='${slider_interior_1}' class='d-block w-100' alt='...'>
				    </div>
				    <div class='carousel-item'>
				      <img src='${slider_interior_2}' class='d-block w-100' alt='...'>
				    </div>
				    <div class='carousel-item'>
				      <img src='${slider_interior_3}' class='d-block w-100' alt='...'>
				    </div>
				    <div class='carousel-item'>
				      <img src='${slider_interior_4}' class='d-block w-100' alt='...'>
				    </div>
				</div>
				  
				<button class='carousel-control-prev' type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide='prev'>
				    <span class='carousel-control-prev-icon' aria-hidden='true'></span>
				    <span class='visually-hidden'>Previous</span>
				</button>
				<button class='carousel-control-next' type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide='next'>
				    <span class='carousel-control-next-icon' aria-hidden='true'></span>
				    <span class='visually-hidden'>Next</span>
				</button>
			</div>
		</div>

		<!-- DESCTOP POP OVER THING-->
		${canvas_background}
	</div>
	</div>
	<!-- DESCTOP END -->


	<!-- PHONE & TABLET-->

	<div class='d-block d-md-none'>
		<div class='thin mt-3 ms-2'>
			<a href='http://temp.decona.ru'>Главная</a> / <a href='http://temp.decona.ru/'>Продукция</a>
		</div>

		<p class='h-center pt-5'>${product_name}</p>
		<center>
          	<p class='fabric-name pb-3'>Ткань: ${fabric_name}
        </center>


        <!-- fabric buttons -->

		<div class='slide-fabric-nav' onClick ='event.stopPropagation()'>  	  
			<img class='slide-fabric-button fabric-var-phone fabric-var CAMBRIDGE_600' id='${collection}_${category}_CAMBRIDGE_600' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/CAMBRIDGE/ICONS/CAMBRIDGE_600.png' onClick ='showDetailsByFabric(event);'>

			<img class='slide-fabric-button fabric-var-phone fabric-var COSMIC_08' id='${collection}_${category}_COSMIC_08' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/COSMIC/COSMIC_08.png' onClick ='showDetailsByFabric(event);'>

			<img class='slide-fabric-button fabric-var-phone fabric-var HARMONY_SILVER' id='${collection}_${category}_HARMONY_SILVER' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/HARMONY/HARMONY_SILVER.png' onClick ='showDetailsByFabric(event);'>  

	    	<img class='slide-fabric-button fabric-var-phone fabric-var JAZZ_01' id='${collection}_${category}_JAZZ_01' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/JAZZ/ICONS/JAZZ_01.png' onClick ='showDetailsByFabric(event);'>

	    	<img class='slide-fabric-button fabric-var-phone fabric-var JAZZ_08' id='${collection}_${category}_JAZZ_08' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/JAZZ/ICONS/JAZZ_08.png' onClick ='showDetailsByFabric(event);'>

	    	<img class='slide-fabric-button fabric-var-phone fabric-var JAZZ_21' id='${collection}_${category}_JAZZ_21' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/JAZZ/ICONS/JAZZ_21.png' onClick ='showDetailsByFabric(event);'>

	    	<img class='slide-fabric-button fabric-var-phone fabric-var PIXEL_FOREST' id='${collection}_${category}_PIXEL_FOREST' src= 'http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/PIXEL/ICONS/PIXEL_FOREST.png' onClick ='showDetailsByFabric(event);'>
	    
	    	<img class='slide-fabric-button fabric-var-phone fabric-var VELUTTO_16' id='${collection}_${category}_VELUTTO_16' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/VELUTTO/ICONS/VELUTTO_16.png' onClick ='showDetailsByFabric(event);'>    	
		</div>
		

		<!-- slider with product -->

		<div id='carouselExampleDark' class='carousel carousel-dark slide px-2' data-bs-ride='carousel'>
		  	<div class='carousel-indicators'>
			    <button type='button' data-bs-target='#carouselExampleDark' data-bs-slide-to='0' class='active' aria-current='true' aria-label='Slide 1'></button>
			    <button type='button' data-bs-target='#carouselExampleDark' data-bs-slide-to='1' aria-label='Slide 2'></button>
			    <button type='button' data-bs-target='#carouselExampleDark' data-bs-slide-to='2' aria-label='Slide 3'></button>
			    <button type='button' data-bs-target='#carouselExampleDark' data-bs-slide-to='3' aria-label='Slide 4'></button>
			    <button type='button' data-bs-target='#carouselExampleDark' data-bs-slide-to='4' aria-label='Slide 5'></button>
		  	</div>
		  	<div class='carousel-inner'>
		    	<div class='carousel-item active' data-bs-interval='10000'>
		      		<img src='${carousel_item_1_mob}' class='d-block w-100' alt='...'>
		    	</div>
		    	<div class='carousel-item' data-bs-interval='2000'>
		      		<img src='${carousel_item_2_mob}' class='d-block w-100' alt='...'>
		    	</div>
		    	<div class='carousel-item'>
		      		<img src='${carousel_item_3_mob}' class='d-block w-100' alt='...'>
		    	</div>
		    	<div class='carousel-item'>
		      		<img src='${carousel_item_4_mob}' class='d-block w-100' alt='...'>
		    	</div>
		    	<div class='carousel-item'>
		      		<img src='${carousel_item_5_mob}' class='d-block w-100' alt='...'>
		    	</div>
		  	</div>
		</div>


		<!-- Name & price -->

		<div class='mt-2'>
			<div class='latte_bg pt-2'>
				<div class='prod-card-model-phone ps-3'>${product_full_name}</div>
				<div class='mt-1 d-flex flex-row'>
					<p class='prod-card-price-phone px-3'>${price_sale} ₽</p>
					<p class='old-price-phone'>${price} ₽</p>
				</div>
			</div>

			<div class='d-flex justify-content-around white btn-prod-card_mob py-2 img-cover cacao_bg'>
				<a class='to-order white p-2' onClick='pushSKUinForm(event);'>
					Заказать
				</a>
				<a class='white p-2' href='http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_DOWNLOADS/3D/CONSONO_mods.zip'>
					3d модель
				</a>
				<a class='white p-2' href='http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_DOWNLOADS/PDF/CONSONO.pdf'>
					PDF
				</a>
			</div>
		</div>	


		<!-- ACCORDION PHONE-->

		<div class='accordion' id='accordionExample'>
		    <div class='accordion-item'><!-- Описание -->
		        <h2 class='accordion-header' id='headingOne'>
		            <button class='accordion-button white_bg' type='button' data-bs-toggle='collapse' data-bs-target='#collapseOne' aria-expanded='true' aria-controls='collapseOne'>
		            Описание
		            </button>
		        </h2>
		        <div id='collapseOne' class='accordion-collapse collapse show' aria-labelledby='headingOne' data-bs-parent='#accordionExample'>
		            <div class='accordion-body'>
		                <p id='description'>
		                	${description}
		                </p>
		          	</div>
		        </div>
		    </div>


		    <div class='accordion-item'><!-- Схема и габариты -->
		        <h2 class='accordion-header' id='headingTwo'>
		            <button class='accordion-button' type='button' data-bs-toggle='collapse' data-bs-target='#collapseTwo' aria-expanded='true' aria-controls='collapseTwo'>
		            Схема и габариты
		            </button>
		        </h2>
		        <div id='collapseTwo' class='accordion-collapse collapse' aria-labelledby='headingTwo' data-bs-parent='#accordionExample'>
		            <div class='accordion-body'>
		            	<div class='container-fluid'>
							<div class='row'>
								<div class='col-md-4 col-sm-12'>
			                		<table class='prod-card-table'>
				                		<tr class='prod-card-table-row'>
											${prod_width}
										</tr>
										<tr class='prod-card-table-row'>
											${prod_depth}
										</tr>
										<tr class='prod-card-table-row'>
											${prod_height}
										</tr>
										<tr class='prod-card-table-row'>
											${prod_weight}
										</tr>
										<tr class='prod-card-table-row'>
											${prod_seat_height}
										</tr>
										<tr class='prod-card-table-row'>
											${prod_seat_width}
										</tr>
										<tr class='prod-card-table-row'>
											${prod_seat_depth}
										</tr>
										<tr class='prod-card-table-row'>
											${prod_back_width}
										</tr>
									</table>

									<!-- button class='btn-outline-gray'>Вся коллекция</button -->

								</div>
								<div class='col-md-4 col-sm-12'>
									${scheme}
									${scheme_2}
								</div>
							</div>
						</div>
					</div>		
		          </div>
		    </div>
		    

		    <div class='accordion-item'><!-- Характеристики -->
		        <h2 class='accordion-header' id='headingThree'>
		            <button class='accordion-button' type='button' data-bs-toggle='collapse' data-bs-target='#collapseThree' aria-expanded='true' aria-controls='collapseThree'>
		            Характеристики
		            </button>
		        </h2>
		        <div id='collapseThree' class='accordion-collapse collapse' aria-labelledby='headingThree' data-bs-parent='#accordionExample'>
		            <div class='accordion-body'>
		                <h4>Основные</h4>
		                <div class='container'>
							<div class='row'>
								<div class='col-md-6 col-sm-12'>
									<table class='prod-card-table'>
										<tr>
											${product_type}
										</tr>
										<tr>
											${transform_type}
										</tr>
										<tr>
											${matress_type}
										</tr>
									</table>
								</div>
								<div class='col-md-6 col-sm-12'>
									<table class='prod-card-table'>
										<tr>
											${product_form}
										</tr>
										<tr>
											${product_style}
										</tr>
										<tr>
											${product_inside}
										</tr>
									</table>
								</div>
								<p class='pt-3'>Конструктивные особенности: ${features}
							</div>
						</div>
		        	</div>
		    	</div>
		    </div>


		    <div class='accordion-item'><!-- Материал обивки -->
		        <h2 class='accordion-header' id='headingFour'>
		            <button class='accordion-button' type='button' data-bs-toggle='collapse' data-bs-target='#collapseFour' aria-expanded='true' aria-controls='collapseFour'>
		            Материал обивки
		            </button>
		        </h2>
		        <div id='collapseFour' class='accordion-collapse collapse' aria-labelledby='headingFour' data-bs-parent='#accordionExample'>
		            <div class='accordion-body'>
		            	<div class='container-fluid'>
							<div class='row'>
								<div class='col-md-8 col-sm-12'>
									<p>${product_fabric_about}
								</div>
								<div class='col-md-4 col-sm-12'>
									<img src='${product_fabric_img}' class='img-fluid'>
								</div>
							</div>
		                	<p class='mt-2' >Больше образцов тканей вы можете посмотреть в наших салонах.
							<a class='my-2' href='http://temp.decona.ru/showrooms/'><button class='btn-outline-gray mt-3'>Адреса салонов</button></a>
			          	</div>
			        </div>
			    </div>
			</div>


		    <div class='accordion-item'><!-- Варианты исполнения ножек -->
		        ${paws_var}
			</div>
	  

		    <div class='accordion-item'><!-- Опции -->
		        <h2 class='accordion-header' id='headingSix'>
		            <button class='accordion-button' type='button' data-bs-toggle='collapse' data-bs-target='#collapseSix' aria-expanded='true' aria-controls='collapseSix'>
		            Опции
		            </button>
		        </h2>
		        <div id='collapseSix' class='accordion-collapse collapse' aria-labelledby='headingSix' data-bs-parent='#accordionExample'>
		            <div class='accordion-body'>
		            	<div>
		                	<p>Вы можете заказать диван как с декоративной отстрочкой внешних швов, так и без неё.
		                	</p>
		                </div>
		                <div class='container-fluid'>
		                	<div class='row'>
								<div class='col-md-6 col-sm-12'>
									<img src='http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_OPTIONS/SEAMS/CONSONO_SEAMS.jpg'>
									<p class='mt-2 thin'>Декоративные швы снаружи
								</div>
								<div class='col-md-6 col-sm-12'>
									<img src='wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_OPTIONS/SEAMS/CONSONO_NOSEAMS.jpg'>
									<p class='mt-2 thin'>Без декоративных швов
								</div>
							</div>
						</div>
		          	</div>
		        </div>
		    </div>
		</div>


		<!-- SLIDER INTERIORS -->

		<div class='banner mt-3'>
			<div id='carouselExampleIndicators' class='carousel slide' data-bs-ride='carousel'>
				<div class='carousel-indicators'>
				    <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='0' class='active' aria-current='true' aria-label='Slide 1'></button>
				    <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='1' aria-label='Slide 2'></button>
				    <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='2' aria-label='Slide 3'></button>
				    <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='3' aria-label='Slide 4'></button>
				</div>

				<div class='carousel-inner'>
				    <div class='carousel-item active'>
				      <img src='${slider_interior_mob_1}' class='d-block w-100' alt='...'>
				    </div>
				    <div class='carousel-item'>
				      <img src='${slider_interior_mob_2}' class='d-block w-100' alt='...'>
				    </div>
				    <div class='carousel-item'>
				      <img src='${slider_interior_mob_3}' class='d-block w-100' alt='...'>
				    </div>
				    <div class='carousel-item'>
				      <img src='${slider_interior_mob_4}' class='d-block w-100' alt='...'>
				    </div>
				</div>
				  
				<button class='carousel-control-prev' type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide='prev'>
				    <span class='carousel-control-prev-icon' aria-hidden='true'></span>
				    <span class='visually-hidden'>Previous</span>
				</button>
				<button class='carousel-control-next' type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide='next'>
				    <span class='carousel-control-next-icon' aria-hidden='true'></span>
				    <span class='visually-hidden'>Next</span>
				</button>
			</div>
		</div>

	</div>
	<!-- end -->

	
	<div class='container-fluid ms-4 mt-5'>
		<p>	Стоимость дивана в нестандартной комплектации рассчитывается в салоне, после выбора клиентом обивки и дополнительных опций. После того, как вы определилисть, подписывается договор, гле прописаны все особенности товара, его доставка и гарантии.</p>
		<!-- button class='btn-outline-gray my-2'>Вся коллекция</button -->
	</div>	
</div>
			`;
		/*console.log(document.getElementById('sofa_details'));*/
		
			} else 
			console.log('Check your life');
		}
	adaptationWidth();
	filterFabricButtons();
	showPopOvers();
}