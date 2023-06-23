/* render new html about the single product */
  			document.getElementById('goods_details').innerHTML = 
			`
<div id='${sku}' class='sku'>
	<!-- Desctop -->
	<div class='container-fluid ms-4 mt-4 d-none d-md-block d-lg-block d-xl-block d-xxl-block'>
		<div class='thin'>
			<a href='http://temp.decona.ru'>Продукция</a> / ${category_ru}
		</div>

		<div class='row'>
			<div class='${category}' id='content_left'>
				<p class='h-center'>${product_name}</p>
				<center>
		      	<p class='fabric-name'>Ткань: ${fabric_name}
		    	</center>

			<!-- fabric buttons -->
				<div class='slide-fabric-nav' onClick ='event.stopPropagation()'>  	  
			    	<img class='slide-fabric-button fabric-var' id='${category}_JAZZ_01' src="http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/JAZZ/ICONS/JAZZ_01.png" onClick ='showDetailsByFabric(event);'>
			    
			    	<img class='slide-fabric-button fabric-var' id='${category}_PIXEL_FOREST' src= "http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/PIXEL/ICONS/PIXEL_FOREST.png" onClick ='showDetailsByFabric(event);'>
			    
			    	<img class='slide-fabric-button fabric-var' id='${category}_CAMBRIDGE_600' src="http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/CAMBRIDGE/ICONS/CAMBRIDGE_600.png" onClick ='showDetailsByFabric(event);'>

			    	<img class='slide-fabric-button fabric-var' id='${category}_JAZZ_21' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/JAZZ/ICONS/JAZZ_21.png' onClick ='showDetailsByFabric(event);'>
			    
				    <img class='slide-fabric-button fabric-var' id='${category}_VELUTTO_32' src="http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/VELUTTO/ICONS/VELUTTO_32.png" onClick ='showDetailsByFabric(event);'>
				</div>

				<div class='d-flex flex-row ms-4 card_icons'>
					<img class = 'is_new_icon' src='${is_new}'>
					<img class = 'available_icon' src='${available_in_showroom}'> 
					<img class = 'available_icon'src='${available_for_delivery_2}'>
				</div>
				<!-- slider with product -->
				<div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="carousel">
					  <div class="carousel-indicators">
					    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
					    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
					    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" aria-label="Slide 3"></button>
					    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="3" aria-label="Slide 4"></button>
					    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="4" aria-label="Slide 5"></button>
					  </div>
					  <div class="carousel-inner">
					    <div class="carousel-item active" data-bs-interval="10000">
					      <img src="${carousel_item_1}" class="d-block w-100" alt="...">
					    </div>
					    <div class="carousel-item" data-bs-interval="2000">
					      <img src="${carousel_item_2}" class="d-block w-100" alt="...">
					    </div>
					    <div class="carousel-item">
					      <img src="${carousel_item_3}" class="d-block w-100" alt="...">
					    </div>
					    <div class="carousel-item">
					      <img src="${carousel_item_4}" class="d-block w-100" alt="...">
					    </div>
					    <div class="carousel-item">
					      <img src="${carousel_item_5}" class="d-block w-100" alt="...">
					    </div>
					  </div>


					  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
					    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
					    <span class="visually-hidden">Previous</span>
					  </button>
					  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
					    <span class="carousel-control-next-icon" aria-hidden="true"></span>
					    <span class="visually-hidden">Next</span>
					  </button>
					</div>  
			</div>

			<div class='no-padding-right' id='content_right'>
				<img class='img-fluid banner' src='${right_sofa_piece}'>
			</div>
		</div>
	</div>
	


	<!-- Phone & Tablet-->
	<div class='container-fluid d-block d-md-none'>
		<div class='thin'>
			<a href='http://temp.decona.ru'>Главная</a> / <a href='http://temp.decona.ru/products/'>Продукция</a>
		</div>

		<p class='h-center pt-2'>${product_name}</p>
		<center>
          	<p class='fabric-name'>Ткань: ${fabric_name}
        </center>

		<div class='slide-fabric-nav' onClick ='event.stopPropagation()'>  	  
	    	<img class='slide-fabric-button fabric-var' id='${category}_JAZZ_01' src="http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/JAZZ/ICONS/JAZZ_01.png" onClick ='showDetailsByFabric(event);'>
	    
	    	<img class='slide-fabric-button fabric-var' id='${category}_PIXEL_FOREST' src= "http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/PIXEL/ICONS/PIXEL_FOREST.png" onClick ='showDetailsByFabric(event);'>
	    
	    	<img class='slide-fabric-button fabric-var' id='${category}_CAMBRIDGE_600' src="http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/CAMBRIDGE/ICONS/CAMBRIDGE_600.png" onClick ='showDetailsByFabric(event);'>

	    	<img class='slide-fabric-button fabric-var' id='${category}_JAZZ_21' src='http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/JAZZ/ICONS/JAZZ_21.png' onClick ='showDetailsByFabric(event);'>
	    
		    <img class='slide-fabric-button fabric-var' id='${category}_VELUTTO_32' src="http://temp.decona.ru/wp-content/uploads/goods_pics/FABRIC/VELUTTO/ICONS/VELUTTO_32.png" onClick ='showDetailsByFabric(event);'>
		</div>

		
		<!-- slider with product -->
		<div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="carousel">
		  <div class="carousel-indicators">
		    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
		    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
		    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" aria-label="Slide 3"></button>
		    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="3" aria-label="Slide 4"></button>
		    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="4" aria-label="Slide 5"></button>
		  </div>
		  <div class="carousel-inner">
		    <div class="carousel-item active" data-bs-interval="10000">
		      <img src="${carousel_item_1_mob}" class="d-block w-100" alt="...">
		    </div>
		    <div class="carousel-item" data-bs-interval="2000">
		      <img src="${carousel_item_2_mob}" class="d-block w-100" alt="...">
		    </div>
		    <div class="carousel-item">
		      <img src="${carousel_item_3_mob}" class="d-block w-100" alt="...">
		    </div>
		    <div class="carousel-item">
		      <img src="${carousel_item_4_mob}" class="d-block w-100" alt="...">
		    </div>
		    <div class="carousel-item">
		      <img src="${carousel_item_5_mob}" class="d-block w-100" alt="...">
		    </div>
		  </div>

		</div>
	</div>
	<!--  -->

	<!-- Name & price -->

	<!-- Desktop -->
	<div class='mb-4 px-5 latte_bg banner container-fluid d-none d-md-block d-lg-block d-xl-block d-xxl-block'>
		<div class="d-flex justify-content-evenly">
			<div class='mt-2 prod-card-model'>${product_full_name}</div>
			<div class='mt-1 d-flex flex-row'>
				<p class='prod-card-price pe-3'>${price_sale} ₽</p>
				<p class='old-price'>${price} ₽</p>
			</div>
			<div class="mt-3 d-flex justify-content-between">
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
	</div>


	<!-- Phone -->
	<div class=' mt-2 d-block d-md-none'>
		<div class='prod-card-model ps-3'>${product_full_name}</div>
		<div class='mt-1 d-flex flex-row'>
				<p class='prod-card-price px-3'>${price_sale} ₽</p>
				<p class='old-price'>${price} ₽</p>
			</div>
		<div class="d-flex justify-content-around white btn-prod-card_mob my-2 img-cover">
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



	<!-- ACCORDION -->

	<!-- desctop -->
	<div class='d-none d-lg-block d-xl-block d-xxl-block' id='desctop-show'>
		<div class="accordion mx-5" id="accordionExample">
		    <div class="accordion-item"><!-- Описание -->
		        <h2 class="accordion-header" id="headingOne">
		            <button class="accordion-button white_bg" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
		            Описание
		            </button>
		        </h2>
		        <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
		            <div class="accordion-body">
		                <p id='description'>
		                	${description}
		                </p>
		          	</div>
		        </div>
		    </div>


		    <div class="accordion-item"><!-- Схема и габариты -->
		        <h2 class="accordion-header" id="headingTwo">
		            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="true" aria-controls="collapseTwo">
		            Схема и габариты
		            </button>
		        </h2>
		        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
		            <div class="accordion-body">
		            	<div class='container-fluid'>
							<div class='row'>
								<div class='col-md-4 col-sm-12'>
			                		<table class='prod-card-table'>
										<tr class='prod-card-table-row'>
											<td>
												<p>Ширина, см
											</td>
											<td>
												<p id='prod_width'>${prod_width}
											</td>
										</tr>
										<tr class='prod-card-table-row'>
											<td>
												<p>Глубина, см
											</td>
											<td>
												<p id='prod_depth'>${prod_depth}
											</td>
										</tr>
										<tr class='prod-card-table-row'>
											<td>
												<p>Высота, см
											</td>
											<td>
												<p id='prod_height'>${prod_height}
											</td>
										</tr>
										<tr class='prod-card-table-row'>
											<td>
												<p>Вес товара, кг
											</td>
											<td>
												<p id='prod_weight'>${prod_weight}
											</td>
										</tr>
										<tr class='prod-card-table-row'>
											<td>
												<p>Высота сидения, см
											</td>
											<td>
												<p id='prod_seat_height'>${prod_seat_height}
											</td>
										</tr>
										<tr class='prod-card-table-row'>
											<td>
											<p>Ширина сидения, см
											</td>
											<td>
												<p id='prod_seat_width'>${prod_seat_width}
											</td>
										</tr>
										<tr class='prod-card-table-row'>
											<td>
												<p>Глубина сидения, см
											</td>
											<td>
												<p id='prod_seat_depth'>${prod_seat_depth}
											</td>
										</tr>
										<tr class='prod-card-table-row'>
											<td>
												<p>Ширина спинки, см
											</td>
											<td>
												<p id='prod_back_width'>${prod_back_width}
											</td>
										</tr>
									</table>

									<!-- button class="btn-outline-gray">Вся коллекция</button -->

								</div>
								<div class='col-md-4 col-sm-12'>
									<img id='' src='${scheme}' class='img-fluid'>
								</div>
								
							</div>
						</div>
					</div>		
		          </div>
		    </div>
		    

		    <div class="accordion-item"><!-- Характеристики -->
		        <h2 class="accordion-header" id="headingThree">
		            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="true" aria-controls="collapseThree">
		            Характеристики
		            </button>
		        </h2>
		        <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample">
		            <div class="accordion-body">
		                <h4>Основные</h4>
		                <div class='accordion-padding'>
							<div class='row'>
								<div class='col-md-6 col-sm-12'>
									<table class='prod-card-table'>
										<tr>
											<td>
												<p class='cacao'>Тип
											</td>
											<td>
												<p class='text-end'>${product_type}
											</td>
										</tr>
										<tr>
											<td>
												<p class='cacao'>Вид раскладывания
											</td>
											<td>
												<p class='text-end'>${transform_type}
											</td>
										</tr>
										<tr>
											<td>
												<p class='cacao'>Тип матраса
											</td>
											<td>
												<p class='text-end'>${matress_type}
											</td>
										</tr>
									</table>
								</div>
								<div class='col-md-6 col-sm-12'>
									<table class='prod-card-table'>
										<tr>
											<td>
												<p class='cacao'>Форма диван
											</td>
											<td>
												<p class='text-end'>${product_form}
											</td>
										</tr>
										<tr>
											<td>
												<p class='cacao'>Стиль дизайна
											</td>
											<td>
												<p class='text-end'>${product_style}
											</td>
										</tr>
										<tr>
											<td>
												<p class='cacao'>Материал наполнителя
											</td>
											<td>
												<p class='text-end'>${product_inside}
											</td>
										</tr>
									</table>
								</div>
								<p class='pt-2'>Конструктивные особенности: ${features}
							</div>
						</div>
		        	</div>
		    	</div>
		    </div>


		    <div class="accordion-item"><!-- Материал обивки -->
		        <h2 class="accordion-header" id="headingFour">
		            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFour" aria-expanded="true" aria-controls="collapseFour">
		            Материал обивки
		            </button>
		        </h2>
		        <div id="collapseFour" class="accordion-collapse collapse" aria-labelledby="headingFour" data-bs-parent="#accordionExample">
		            <div class="accordion-body">
		            	<div class='container-fluid'>
							<div class='row'>
								<div class='col-md-8 col-sm-12'>
									<p>${product_fabric_about}
									<p>Обращаем Ваше внимание, что реальный цвет ткани может значительно отличаться от изображения на экране. Это зависит от индивидуальных настроек монитора и восприятия цвета. Поэтому при заказе ткани ориентируйтесь на реальные образцы.
		                			<p class='pt-2'>Больше образцов тканей вы можете посмотреть в наших салонах.
									<p><a href='http://temp.decona.ru/showrooms/'><button class='btn-outline-gray'>Адреса салонов</button></a>
								</div>
								<div class='col-md-4 col-sm-12'>
									<img src="${product_fabric_img}" class='img-fluid'>
								</div>
							</div>	
			          	</div>
			        </div>
			    </div>
			</div>


		    <div class="accordion-item"><!-- Варианты исполнения ножек -->
		        <h2 class="accordion-header" id="headingFive">
		            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFive" aria-expanded="true" aria-controls="collapseFive">
		            Варианты исполнения ножек
		            </button>
		        </h2>
		        <div id="collapseFive" class="accordion-collapse collapse" aria-labelledby="headingFive" data-bs-parent="#accordionExample">
		            <div class="accordion-body">
		            	<div class="container-fluid">
							<div class="row">
								<div class="col-md-6 col-sm-12">
									<p>Стильные конусовидные металлические ножки как тонкий оммаж дизайну славных 1960-х: времени первых шагов человечества в космическом пространстве.
									<p><img src="http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_LEG_CAMBRIDGE_600.jpg" alt="..." class="mt-5 w-50">	
								
								</div>			 
							</div>
		          		</div>
		        	</div>
				</div>
			</div>
	  

		    <div class="accordion-item"><!-- Опции -->
		        <h2 class="accordion-header" id="headingSix">
		            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseSix" aria-expanded="true" aria-controls="collapseSix">
		            Опции
		            </button>
		        </h2>
		        <div id="collapseSix" class="accordion-collapse collapse" aria-labelledby="headingSix" data-bs-parent="#accordionExample">
		            <div class="accordion-body">
		            	<div>
		                	<p class='mb-2'>Вы можете заказать диван как с декоративной отстрочкой внешних швов, так и без неё.
		                	</p>
		                </div>
		                <div class='container-fluid'>
		                	<div class='row'>
								<div class='ps-5 col-md-6 col-sm-12'>
									<p>Декоративные швы снаружи
									<img src="http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_OPTIONS/SEAMS/CONSONO_SEAMS.jpg">
								</div>
								<div class='pe-5 col-md-6 col-sm-12'>
									<p>Без декоративных швов
									<img src="wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_OPTIONS/SEAMS/CONSONO_NOSEAMS.jpg">
								</div>
							</div>
						</div>
		          	</div>
		        </div>
		    </div>
		</div>
	</div>

	<!-- phone -->
	<div class='d-block d-lg-none'>
		<div class="accordion" id="accordionExample">

		    <div class="accordion-item"><!-- Описание -->
		        <h2 class="accordion-header" id="headingOne">
		            <button class="accordion-button white_bg" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
		            Описание
		            </button>
		        </h2>
		        <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
		            <div class="accordion-body">
		                <p id='description'>
		                	${description}
		                </p>
		          	</div>
		        </div>
		    </div>


		    <div class="accordion-item"><!-- Схема и габариты -->
		        <h2 class="accordion-header" id="headingTwo">
		            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="true" aria-controls="collapseTwo">
		            Схема и габариты
		            </button>
		        </h2>
		        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
		            <div class="accordion-body">
		            	<div class='container-fluid'>
							<div class='row'>
								<div class='col-md-4 col-sm-12'>
			                		<table class='prod-card-table'>
										<td>
												<p>Ширина, см
											</td>
											<td>
												<p id='prod_width'>${prod_width}
											</td>
										</tr>
										<tr class='prod-card-table-row'>
											<td>
												<p>Глубина, см
											</td>
											<td>
												<p id='prod_depth'>${prod_depth}
											</td>
										</tr>
										<tr class='prod-card-table-row'>
											<td>
												<p>Высота, см
											</td>
											<td>
												<p id='prod_height'>${prod_height}
											</td>
										</tr>
										<tr class='prod-card-table-row'>
											<td>
												<p>Вес товара, кг
											</td>
											<td>
												<p id='prod_weight'>${prod_weight}
											</td>
										</tr>
										<tr class='prod-card-table-row'>
											<td>
												<p>Высота сидения, см
											</td>
											<td>
												<p id='prod_seat_height'>${prod_seat_height}
											</td>
										</tr>
										<tr class='prod-card-table-row'>
											<td>Ширина сидения, см
											</td>
											<td>
												<p id='prod_seat_width'>${prod_seat_width}
											</td>
										</tr>
										<tr class='prod-card-table-row'>
											<td>
												<p>Глубина сидения, см
											</td>
											<td>
												<p id='prod_seat_depth'>${prod_seat_depth}
											</td>
										</tr>
										<tr class='prod-card-table-row'>
											<td>
												<p>Ширина спинки, см
											</td>
											<td>
												<p id='prod_back_width'>${prod_back_width}
											</td>
										</tr>
									</table>

									<!-- button class="btn-outline-gray">Вся коллекция</button -->

								</div>
								<div class='col-md-4 col-sm-12'>
									<img id='' src='${scheme}' class='img-fluid'>
								</div>
							</div>
						</div>
					</div>		
		          </div>
		    </div>
		    

		    <div class="accordion-item"><!-- Характеристики -->
		        <h2 class="accordion-header" id="headingThree">
		            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="true" aria-controls="collapseThree">
		            Характеристики
		            </button>
		        </h2>
		        <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample">
		            <div class="accordion-body">
		                <h4>Основные</h4>
		                <div class='container'>
							<div class='row'>
								<div class='col-md-5 col-sm-12'>
									<table class='prod-card-table'>
										<tr>
											<td>
												<p class='cacao'>Тип
											</td>
											<td>
												<p class='text-end'>${product_type}
											</td>
											</tr>
											<tr>
											<td>
												<p class='cacao'>Вид раскладывания
											</td>
											<td>
												<p class='text-end'>${transform_type}
											</td>
											</tr>
											<tr>
											<td>
												<p class='cacao'>Тип матраса
											</td>
											<td>
												<p class='text-end'>${matress_type}
											</td>
										</tr>
									</table>
								</div>
								<div cass='col d-md-block d-none'></div>
								<div class='col-md-5 col-sm-12'>
									<table class='prod-card-table'>
										<tr>
											<td>
												<p class='cacao'>Форма диван
											</td>
											<td>
												<p class='text-end'>${product_form}
											</td>
										</tr>
										<tr>
											<td>
												<p class='cacao'>Стиль дизайна
											</td>
											<td>
												<p class='text-end'>${product_style}
											</td>
										</tr>
										<tr>
											<td>
												<p class='cacao'>Материал наполнителя
											</td>
											<td>
												<p class='text-end'>${product_inside}
											</td>
										</tr>
									</table>
								</div>
								<p class='mt-2'>Конструктивные особенности: ${features}
							</div>
						</div>
		        	</div>
		    	</div>
		    </div>


		    <div class="accordion-item"><!-- Материал обивки -->
		        <h2 class="accordion-header" id="headingFour">
		            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFour" aria-expanded="true" aria-controls="collapseFour">
		            Материал обивки
		            </button>
		        </h2>
		        <div id="collapseFour" class="accordion-collapse collapse" aria-labelledby="headingFour" data-bs-parent="#accordionExample">
		            <div class="accordion-body">
		            	<div class='container-fluid'>
							<div class='row'>
								<div class='col-md-8 col-sm-12'>
									<p>${product_fabric_about}
								</div>
								<div class='col-md-4 col-sm-12'>
									<img src="${product_fabric_img}" class='img-fluid'>
								</div>
							</div>
		                	<p class='mt-2' >Больше образцов тканей вы можете посмотреть в наших салонах.
							<a class='my-2' href='http://temp.decona.ru/showrooms/'><button class='btn-outline-gray'>Адреса салонов</button></a>
			          	</div>
			        </div>
			    </div>
			</div>


		    <div class="accordion-item"><!-- Варианты исполнения ножек -->
		        <h2 class="accordion-header" id="headingFive">
		            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFive" aria-expanded="true" aria-controls="collapseFive">
		            Варианты исполнения ножек
		            </button>
		        </h2>
		        <div id="collapseFive" class="accordion-collapse collapse" aria-labelledby="headingFive" data-bs-parent="#accordionExample">
		            <div class="accordion-body">
		            	<div class="container-fluid">
							<div class="row">
								<div class="col-md-6 col-sm-12">
									<p>Стильные конусовидные металлические ножки как тонкий оммаж дизайну славных 1960-х: времени первых шагов человечества в космическом пространстве.
									<p><img src="http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_LEG_CAMBRIDGE_600.jpg" alt="..." class="mt-5 w-50">	
								
								</div>			 
							</div>
		          		</div>
		        	</div>
				</div>
			</div>
	  

		    <div class="accordion-item"><!-- Опции -->
		        <h2 class="accordion-header" id="headingSix">
		            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseSix" aria-expanded="true" aria-controls="collapseSix">
		            Опции
		            </button>
		        </h2>
		        <div id="collapseSix" class="accordion-collapse collapse" aria-labelledby="headingSix" data-bs-parent="#accordionExample">
		            <div class="accordion-body">
		            	<div>
		                	<p>Вы можете заказать диван как с декоративной отстрочкой внешних швов, так и без неё.
		                	</p>
		                </div>
		                <div class='container-fluid'>
		                	<div class='row'>
								<div class='col-md-6 col-sm-12'>
									<img src="http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_OPTIONS/SEAMS/CONSONO_SEAMS.jpg">
									<p class="mt-2 thin">Декоративные швы снаружи
								</div>
								<div class='col-md-6 col-sm-12'>
									<img src="wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_OPTIONS/SEAMS/CONSONO_NOSEAMS.jpg">
									<p class="mt-2 thin">Без декоративных швов
								</div>
							</div>
						</div>
		          	</div>
		        </div>
		    </div>
		</div>
	</div>
	<!-- the end of accordion part -->


<!-- Slider with interiors DESCTOP -->
	<div class='mt-5 banner d-none d-md-block d-lg-block d-xl-block d-xxl-block'>
		<div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
			<div class="carousel-indicators">
			    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="carousel-btn-bottom active" aria-current="true" aria-label="Slide 1"></button>
			    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" class="carousel-btn-bottom" aria-label="Slide 2"></button>
			    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" class="carousel-btn-bottom" aria-label="Slide 3"></button>
			     <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" class="carousel-btn-bottom" aria-label="Slide 4"></button>
			</div>

		 	<div class="carousel-inner" onmousemove='showPopOvers();'>
			    <div class="carousel-item active">
			      <img src="http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_INTERIORS/CONSONO_1.jpg" class="d-block w-100" alt="...">
			    </div>
			    <div class="carousel-item">
			      <img src="http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_INTERIORS/CONSONO_2.jpg" alt="...">
			    </div>
			    <div class="carousel-item">
			      <img src="http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_INTERIORS/CONSONO_3.jpg" alt="...">
			    </div>
			    <div class="carousel-item">
			      <img src="http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_INTERIORS/CONSONO_4.jpg" alt="...">
			    </div>
			</div>

			 <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
			    <span class="carousel-control-prev-icon pt-5" aria-hidden="true"></span>
			    <span class="visually-hidden">Previous</span>
			  </button>
			  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
			    <span class="carousel-control-next-icon pt-5" aria-hidden="true"></span>
			    <span class="visually-hidden">Next</span>
			  </button>
		</div>  
	</div>
	<!-- Slider DESCTOP end -->

	<!-- Slider with interiors PHONE & TABLET  -->
	<div class='mt-3 banner d-block d-md-none'>
		<div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
			<div class="carousel-indicators">
			    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="carousel-btn-bottom active" aria-current="true" aria-label="Slide 1"></button>
			    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" class="carousel-btn-bottom" aria-label="Slide 2"></button>
			    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" class="carousel-btn-bottom" aria-label="Slide 3"></button>
			     <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" class="carousel-btn-bottom" aria-label="Slide 4"></button>
			</div>

		 	<div class="carousel-inner" onmousemove='showPopOvers();'>
			    <div class="carousel-item active">
			      <img src="http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_INTERIORS_mob/CONSONO_1_mob.jpg" class="d-block w-100" alt="...">
			    </div>
			    <div class="carousel-item">
			      <img src="http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_INTERIORS_mob/CONSONO_2_mob.jpg" alt="...">
			    </div>
			    <div class="carousel-item">
			      <img src="http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_INTERIORS_mob/CONSONO_3_mob.jpg" alt="...">
			    </div>
			    <div class="carousel-item">
			      <img src="http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_INTERIORS_mob/CONSONO_4_mob.jpg" alt="...">
			    </div>
			</div>

			 <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
			    <span class="carousel-control-prev-icon pt-5" aria-hidden="true"></span>
			    <span class="visually-hidden">Previous</span>
			  </button>
			  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
			    <span class="carousel-control-next-icon pt-5" aria-hidden="true"></span>
			    <span class="visually-hidden">Next</span>
			  </button>
		</div>  
	</div>
	<!-- Slider PHONE end -->


	<!-- DESCTOP POP OVER THING START -->
	<div class='popOverBlock pt-5 d-none d-lg-block d-xl-block d-xxl-block'>
		<canvas id="canvasBig" style="display:block" width='1600' height='800'></canvas>

		<div class = 'popOvers'>	
	        <div id='popAboutStitchesBig'>
	          	<div class='card' style='width: 15rem;'>
	            	<img src='http://temp.decona.ru/wp-content/uploads/2023/02/Detail_1-1.png' class='card-img-top'>
	            	<div class='card-body'>
	             		<p class='card-text'>Мы прошиваем наши диваны турецкими мебельными нитями марки POLYART. Это синтетические армированные  нити с полиэфирной оплёткой. Нити обладают высокой прочностью и устойчивы к истиранию. </p>
	            	</div>
	         	</div>
	       	</div>

	       	<div id='popAboutPillowBig'>
	          	<div class='card' style='width: 15rem;'>
	           		<img src='http://temp.decona.ru/wp-content/uploads/2023/02/Detail_1-1.png' class='card-img-top'>
	            	<div class='card-body'>
	              		<p class='card-text'>Подушка может лежать на диване. А может быть сброшена кошкой. Ещё ей можно драться. </p>
	            	</div>
	         	</div>
	       	</div>

	       <div id='popAboutFrontBig'>
	          	<div class='card' style='width: 15rem;'>
	            	<img src='http://temp.decona.ru/wp-content/uploads/2023/02/Detail_1-1.png' class='card-img-top'>
	            	<div class='card-body'>
	              		<p class='card-text'>Край дивана. Наверное, здесь что-то о диванном внутреннем мире - какие там пружины внутри хитрые. Или нет? </p>
		            </div>
		         </div>
	       	</div>

	       	<div id='popAboutBackBig'>
	          	<div class='card' style='width: 15rem;'>
	            	<img src='http://temp.decona.ru/wp-content/uploads/2023/02/Detail_1-1.png' class='card-img-top'>
	            	<div class='card-body'>
	              		<p class='card-text'>Спинка дивана. Наверное, здесь о наполнителе - какой он белый, пушистый и высокотехнологичный. Или нет? </p>
	            	</div>
	         	</div>
	       	</div>

	       	<div id='popAboutPawBig'>
	          	<div class='card' style='width: 15rem;'>
	            	<img src='http://temp.decona.ru/wp-content/uploads/2023/02/Detail_1-1.png' class='card-img-top'>
	            	<div class='card-body'>
	              		<p class='card-text'>Диванная ножка. Наверное, здесь о том, что она из дуба 4 сортов. Или нет? </p>
	            	</div>
	         	</div>
	       	</div>
	    </div>
	</div> 
	<div class='container-fluid ms-4 mt-4'>
		<p>	Стоимость дивана в нестандартной комплектации рассчитывается в салоне, после выбора клиентом обивки и дополнительных опций. После того, как вы определилисть, подписывается договор, гле прописаны все особенности товара, его доставка и гарантии.</p>
		<!-- button class="btn-outline-gray my-2">Вся коллекция</button>
	</div>	
</div>
			`; 
		} /*else console.log('Check your json!');*/
	}
	showPopOvers();
	adaptationWidth();

}