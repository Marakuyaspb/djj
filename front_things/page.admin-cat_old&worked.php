if(isset($_POST['create_prod_pages'])){
	// Step 1: Connect to the MySQL database
	$servername = 'localhost';
	$username = 'deconaru';
	$password = 'WULk_JT76BF7KULL';
	$dbname = 'deconaru';

	$conn = mysqli_connect("localhost", "deconaru", "WULk_JT76BF7KULL", "deconaru");

	// Check connection
	if (!$conn) {
		//print_r 'Sorry. Connection failed';

	    die('Connection failed: ' . mysqli_connect_error());

	}

	// Step 2: Fetch data from the database
	$sql = 'SELECT * FROM goods_wonder';
	$result = mysqli_query($conn, $sql);

	// Step 3: Create new HTML pages
	$template = "
	    <?php
	    get_header('new'); 
	    ?>

	    <div id='%s' class='sku'>
	        <!-- Desctop -->
	        <div class='container-fluid mt-4 d-none d-md-block d-lg-block d-xl-block d-xxl-block'>
	            <div class='thin ms-4'><a href='http://temp.decona.ru/products/'>Продукция</a> / <a href='http://temp.decona.ru/line-sofas/'>Прямые диваны</a>
	            </div>

	            <div class='row'>
	                <div class='col-md-8'>
	                    <p class='h-center'>%s</p>
	                    <center>
	                    <p class='fabric-name pt-4'>Ткань: %s
	                    </center>
	                <!-- fabric buttons -->
	                    <div class='slide-fabric-nav' onClick ='event.stopPropagation()'>     
	                        <img class='slide-fabric-button fabric-var' id='%s_jazz_01' src='http://temp.decona.ru/p-content/uploads/goods_pics/FABRIC/JAZZ/ICONS/JAZZ_01.png' onClick ='showDetailsByFabric(event);'>
	                    
	                        <img class='slide-fabric-button fabric-var' id='%s_jazz_21' src='http://temp.decona.ru/p-content/uploads/goods_pics/FABRIC/JAZZ/ICONS/JAZZ_21.png' onClick ='showDetailsByFabric(event);'>
	                    
	                        <img class='slide-fabric-button fabric-var' id='%s_pixel_forest' src= 'http://temp.decona.ru/p-content/uploads/goods_pics/FABRIC/PIXEL/ICONS/PIXEL_FOREST.png' onClick ='showDetailsByFabric(event);'>
	                    
	                        <img class='slide-fabric-button fabric-var' id='%s_cambridge_600' src='http://temp.decona.ru/p-content/uploads/goods_pics/FABRIC/CAMBRIDGE/ICONS/CAMBRIDGE_600.png' onClick ='showDetailsByFabric(event);'>
	                    
	                        <img class='slide-fabric-button fabric-var' id='%s_velutto_32' src='http://temp.decona.ru/p-content/uploads/goods_pics/FABRIC/JAZZ/ICONS/JAZZ_08.png' onClick ='showDetailsByFabric(event);'>
	                    </div>
	                    <div class='ms-4'>
	                        <img class = 'is_new_icon' src='%s'>
	                        <img class = 'available_icon' src='%s'> 
	                        <img class = 'available_icon'src='%s'>
	                    </div>
	                <!-- slider with product --''
	                    <div id='carouselExampleIndicators' class='carousel slide' data-bs-ride='carousel'>
	                        <div class='carousel-indicators'>
	                            <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='0' class='active carousel-btn-bottom carousel-goods' aria-current='true' aria-label='Slide 1'></button>
	                            <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='1' class='carousel-btn-bottom carousel-goods' aria-label='Slide 2'></button>
	                            <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='2' class='carousel-btn-bottom carousel-goods' aria-label='Slide 3'></button>
	                            <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='3' class='carousel-btn-bottom carousel-goods' aria-label='Slide 4'></button>
	                            <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='4' class='carousel-btn-bottom carousel-goods' aria-label='Slide 5'></button>
	                        </div>

	                        <div class='carousel-inner'>
	                            <div class='carousel-item active'>
	                                <img src='%s' class='d-block w-100' alt='...'>
	                            </div>
	                            <div class='carousel-item'>
	                                <img src='%s' class='d-block w-100' alt='...'>
	                            </div>
	                            <div class='carousel-item'>
	                                <img src='%s' class='d-block w-100' alt='...'>
	                            </div>
	                            <div class='carousel-item'>
	                                <img src='%s' class='d-block w-100' alt='...'>
	                            </div>
	                            <div class='carousel-item'>
	                                <img src='%s' class='d-block w-100' alt='...'>
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

	                <div class='col-md-4 no-padding-right'>
	                    <img class='img-fluid banner' src='%s'>
	                </div>
	            </div>
	        </div>
	        


	        <!-- Phone & Tablet-->
	        <div class='container-fluid mt-5 d-block d-md-none'>
	            <div class='thin ms-4'><a href='http://temp.decona.ru/products/'>Продукция</a> / <a href='http://temp.decona.ru/line-sofas/'>Прямые диваны</a>
	            </div>

	            <center>
	                <p class='fabric-name pt-4'>Ткань: %s
	            </center>

	            <div class='slide-fabric-nav' onClick ='event.stopPropagation()'>     
	                <img class='slide-fabric-button fabric-var' id='%s_jazz_01' src='http://temp.decona.ru/wp-content/uploads/2023/02/Jazz-01-copy-1.png' onClick ='showDetailsByFabric(event);'>
	            
	                <img class='slide-fabric-button fabric-var' id='%s_jazz_08'src='http://temp.decona.ru/wp-content/uploads/2023/02/Jazz-08-copy-1.png' onClick ='showDetailsByFabric(event);'>
	            
	                <img class='slide-fabric-button fabric-var' id='%s_jazz_21' src= 'http://temp.decona.ru/wp-content/uploads/2023/02/Jazz-21-copy-1.png' onClick ='showDetailsByFabric'>
	            
	                <img class='slide-fabric-button fabric-var' id='%s_velutto_16' src='http://temp.decona.ru/wp-content/uploads/2023/02/VElutto-16-1.png' onClick ='showDetailsByFabric(event);'>
	            
	                <img class='slide-fabric-button fabric-var' id='%s_velutto_32' src='http://temp.decona.ru/wp-content/uploads/2023/02/VElutto-32-copy-1.png' onClick ='showDetailsByFabric(event);'>    
	            </div>

	            <div class='ms-4 d-block d-sm-none'>
	                <img class = 'is_new_icon' src='%s'>
	                <img class = 'available_icon' src='%s'> 
	                <img class = 'available_icon'src='%s'>
	            </div>

	            <!-- slider with product -->
	                <div id='carouselExampleIndicators' class='carousel slide' data-bs-ride='carousel'>
	                    <div class='carousel-indicators'>
	                        <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='0' class='active carousel-btn-bottom carousel-goods' aria-current='true' aria-label='Slide 1'></button>
	                        <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='1' class='carousel-btn-bottom carousel-goods' aria-label='Slide 2'></button>
	                        <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='2' class='carousel-btn-bottom carousel-goods' aria-label='Slide 3'></button>
	                        <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='3' class='carousel-btn-bottom carousel-goods' aria-label='Slide 4'></button>
	                        <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='4' class='carousel-btn-bottom carousel-goods' aria-label='Slide 5'></button>
	                    </div>

	                    <div class='carousel-inner'>
	                        <div class='carousel-item active'>
	                            <img src='%s' class='d-block w-100' alt='...'>
	                        </div>
	                        <div class='carousel-item'>
	                            <img src='%s' class='d-block w-100' alt='...'>
	                        </div>
	                        <div class='carousel-item'>
	                            <img src='%s' class='d-block w-100' alt='...'>
	                        </div>
	                        <div class='carousel-item'>
	                            <img src='%s' class='d-block w-100' alt='...'>
	                        </div>
	                        <div class='carousel-item'>
	                            <img src='%s' class='d-block w-100' alt='...'>
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
	        <!--  -->

	        <!-- Name & price -->

	        <!-- Desktop -->
	        <div class='mb-4 px-5 latte_bg banner container-fluid d-none d-md-block d-lg-block d-xl-block d-xxl-block'>
	            <div class='d-flex justify-content-evenly'>
	                <div class='mt-2 prod-card-model'>%s</div>
	                <div class='mt-1'>
	                    <p class='prod-card-price'>%s</p>
	                    <p class='old-price'>%s</p>
	                </div>
	                <div class='mt-3 d-flex justify-content-between'>
	                    <a class='' href='#'>
	                        <button class='to-order white btn-prod-card' onClick='pushSKUinForm(event);'>
	                            Заказать
	                        </button>
	                    </a>
	                    <a class='white' href='#'>
	                        <button class='white btn-prod-card'>
	                            3d модель
	                        </button>
	                    </a>
	                    <a class='white' href='#'>
	                        <button class='white btn-prod-card'>
	                            PDF
	                        </button>
	                    </a>
	                </div>
	            </div>
	        </div>


	        <!-- Phone -->
	        <div class=' mt-2 d-block d-md-none'>
	            <div class='ps-3'>%s</div>
	            <div class='mt-1'>
	                    <p class='prod-card-price'>%s</p>
	                    <p class='old-price'>%s</p>
	                </div>
	            <div class='d-flex justify-content-around white btn-prod-card my-2 img-cover'>
	                    <a class='to-order white p-2' onClick='pushSKUinForm(event);'>
	                        Заказать
	                    </a>
	                    <a class='white p-2' href='#'>
	                        3d модель
	                    </a>
	                    <a class='white p-2' href='#'>
	                        PDF
	                    </a>
	                </div>
	        </div>  



	        <!-- ACCORDION -->

	        <!-- desctop -->
	        <div class='d-none d-lg-block d-xl-block d-xxl-block' id='desctop-show'>
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
	                                %s
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
	                                                <td>
	                                                    <p>Ширина, см
	                                                </td>
	                                                <td>
	                                                    <p id='prod_width'>%s
	                                                </td>
	                                            </tr>
	                                            <tr class='prod-card-table-row'>
	                                                <td>
	                                                    <p>Глубина, см
	                                                </td>
	                                                <td>
	                                                    <p id='prod_depth'>%s
	                                                </td>
	                                            </tr>
	                                            <tr class='prod-card-table-row'>
	                                                <td>
	                                                    <p>Высота, см
	                                                </td>
	                                                <td>
	                                                    <p id='prod_height'>%s
	                                                </td>
	                                            </tr>
	                                            <tr class='prod-card-table-row'>
	                                                <td>
	                                                    <p>Вес товара, кг
	                                                </td>
	                                                <td>
	                                                    <p id='prod_weight'>%s
	                                                </td>
	                                            </tr>
	                                            <tr class='prod-card-table-row'>
	                                                <td>
	                                                    <p>Высота сидения, см
	                                                </td>
	                                                <td>
	                                                    <p id='prod_seat_height'>%s
	                                                </td>
	                                            </tr>
	                                            <tr class='prod-card-table-row'>
	                                                <td>Ширина сидения, см
	                                                </td>
	                                                <td>
	                                                    <p id='prod_seat_width'>%s
	                                                </td>
	                                            </tr>
	                                            <tr class='prod-card-table-row'>
	                                                <td>
	                                                    <p>Глубина сидения, см
	                                                </td>
	                                                <td>
	                                                    <p id='prod_seat_depth'>%s
	                                                </td>
	                                            </tr>
	                                            <tr class='prod-card-table-row'>
	                                                <td>
	                                                    <p>Ширина спинки, см
	                                                </td>
	                                                <td>
	                                                    <p id='prod_back_width'>%s
	                                                </td>
	                                            </tr>
	                                        </table>
	                                    </div>
	                                    <div class='col-md-4 col-sm-12'>
	                                        <img id='' src='http://temp.decona.ru/wp-content/uploads/2023/02/Размеры.jpg' class='img-fluid'>
	                                    </div>
	                                    <div class='col-md-4 col-sm-12'>    
	                                        <img id='' src='http://temp.decona.ru/wp-content/uploads/2023/02/Механизм.jpg' class='img-fluid'>
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
	                                                <td>
	                                                    <p class='cacao'>Тип
	                                                </td>
	                                                <td>
	                                                    <p class='text-end'>%s
	                                                </td>
	                                            </tr>
	                                            <tr>
	                                                <td>
	                                                    <p class='cacao'>Вид раскладывания
	                                                </td>
	                                                <td>
	                                                    <p class='text-end'>%s
	                                                </td>
	                                            </tr>
	                                            <tr>
	                                                <td>
	                                                    <p class='cacao'>Тип матраса
	                                                </td>
	                                                <td>
	                                                    <p class='text-end'>%s
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
	                                                    <p class='text-end'>%s
	                                                </td>
	                                            </tr>
	                                            <tr>
	                                                <td>
	                                                    <p class='cacao'>Стиль дизайна
	                                                </td>
	                                                <td>
	                                                    <p class='text-end'>%s
	                                                </td>
	                                            </tr>
	                                            <tr>
	                                                <td>
	                                                    <p class='cacao'>Материал наполнителя
	                                                </td>
	                                                <td>
	                                                    <p class='text-end'>%s
	                                                </td>
	                                            </tr>
	                                        </table>
	                                    </div>
	                                    <p>Конструктивные особенности: %s
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
	                                        <p>$%s
	                                        <p>Обращаем Ваше внимание, что реальный цвет ткани может значительно отличаться от изображения на экране. Это зависит от индивидуальных настроек монитора и восприятия цвета. Поэтому при заказе ткани ориентируйтесь на реальные образцы.
	                                        <p class='pt-2'>Больше образцов тканей вы можете посмотреть в наших салонах.
	                                        <p><a href='http://temp.decona.ru/showrooms/'><button class='btn-outline-gray'>Адреса салонов</button></a>
	                                    </div>
	                                    <div class='col-md-4 col-sm-12'>
	                                        <img src='%s' class='img-fluid'>
	                                    </div>
	                                </div>  
	                            </div>
	                        </div>
	                    </div>
	                </div>


	                <div class='accordion-item'><!-- Варианты исполнения ножек -->
	                    <h2 class='accordion-header' id='headingFive'>
	                        <button class='accordion-button' type='button' data-bs-toggle='collapse' data-bs-target='#collapseFive' aria-expanded='true' aria-controls='collapseFive'>
	                        Варианты исполнения ножек
	                        </button>
	                    </h2>
	                    <div id='collapseFive' class='accordion-collapse collapse' aria-labelledby='headingFive' data-bs-parent='#accordionExample'>
	                        <div class='accordion-body'>
	                            <div class='container-fluid'>
	                                <p>Массив дуба - природный материал в неповторимым рисунком
	                                <p class='cacao small-text'>В вашем изделии узор будет уникальным и может отличаться отпредставленных
	                            </div>
	                            <div class='container-fluid'>
	                                <div class='row'>
	                                    <div class='col-md-3 col-sm-6'>
	                                        <p class='major-text'>Sand</p>
	                                        <img src='http://temp.decona.ru/wp-content/uploads/2023/02/Leg_sand.png' class='card-img-top' alt='...'>
	                                    </div>
	                                    <div class='col-md-3 col-sm-6'>
	                                        <p class='major-text'>Black</p>
	                                        <img src='http://temp.decona.ru/wp-content/uploads/2023/02/Leg_Black.png' class='card-img-top' alt='...'>                 
	                                    </div>
	                                    <div class='col-md-3 col-sm-6'>
	                                        <p class='major-text'>Brandy</p>
	                                        <img src='http://temp.decona.ru/wp-content/uploads/2023/02/Leg_Brandy.png' class='card-img-top' alt='...'>
	                                    </div>
	                                    <div class='col-md-3 col-sm-6'>
	                                        <p class='major-text'>Arctic</p>
	                                        <img src='http://temp.decona.ru/wp-content/uploads/2023/02/Leg_Arctik.png' class='card-img-top' alt='...'>
	                                    </div>
	                                </div>
	                            </div>
	                        </div>
	                    </div>
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
	                                <p>Вы можете заказать как диван с декоративными утяжками на сидении, 
	                                <p>приспинных подушках и подлокотниках, так и без них
	                                </p>
	                            </div>
	                            <div class='container-fluid'>
	                                <div class='row'>
	                                    <div class='ps-5 col-md-6 col-sm-12'>
	                                        <p>С утяжками
	                                        <img src='http://temp.decona.ru/wp-content/uploads/2023/02/Seat_WOs-4.png'>
	                                    </div>
	                                    <div class='pe-5 col-md-6 col-sm-12'>
	                                        <p>Без утяжек
	                                        <img src='http://temp.decona.ru/wp-content/uploads/2023/02/Seat_WOs-4.png'>
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
	                                %s
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
	                                            <td>
	                                                <p>Ширина, см
	                                            </td>
	                                            <td>
	                                                <p id='prod_width'>%s
	                                            </td>
	                                        </tr>
	                                        <tr class='prod-card-table-row'>
	                                            <td>
	                                                <p>Глубина, см
	                                            </td>
	                                            <td>
	                                                <p id='prod_depth'>%s
	                                            </td>
	                                        </tr>
	                                        <tr class='prod-card-table-row'>
	                                            <td>
	                                                <p>Высота, см
	                                            </td>
	                                            <td>
	                                                <p id='prod_height'>%s
	                                            </td>
	                                        </tr>
	                                        <tr class='prod-card-table-row'>
	                                            <td>
	                                                <p>Вес товара, кг
	                                            </td>
	                                            <td>
	                                                <p id='prod_weight'>%s
	                                            </td>
	                                        </tr>
	                                        <tr class='prod-card-table-row'>
	                                            <td>
	                                                <p>Высота сидения, см
	                                            </td>
	                                            <td>
	                                                <p id='prod_seat_height'>%s
	                                            </td>
	                                        </tr>
	                                        <tr class='prod-card-table-row'>
	                                            <td>Ширина сидения, см
	                                            </td>
	                                            <td>
	                                                <p id='prod_seat_width'>%s
	                                            </td>
	                                        </tr>
	                                        <tr class='prod-card-table-row'>
	                                            <td>
	                                                <p>Глубина сидения, см
	                                            </td>
	                                            <td>
	                                                <p id='prod_seat_depth'>%s
	                                            </td>
	                                        </tr>
	                                        <tr class='prod-card-table-row'>
	                                            <td>
	                                                <p>Ширина спинки, см
	                                            </td>
	                                            <td>
	                                                <p id='prod_back_width'>%s
	                                            </td>
	                                        </tr>
	                                        </table>
	                                    </div>
	                                    <div class='col-md-4 col-sm-12'>
	                                        <img id='' src='http://temp.decona.ru/wp-content/uploads/2023/02/Размеры.jpg' class='img-fluid'>
	                                    </div>
	                                    <div class='col-md-4 col-sm-12'>    
	                                        <img id='' src='http://temp.decona.ru/wp-content/uploads/2023/02/Механизм.jpg' class='img-fluid'>
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
	                                                <td>
	                                                    <p class='cacao'>Тип
	                                                </td>
	                                                <td>
	                                                    <p class='text-end'>%s
	                                                </td>
	                                                </tr>
	                                                <tr>
	                                                <td>
	                                                    <p class='cacao'>Вид раскладывания
	                                                </td>
	                                                <td>
	                                                    <p class='text-end'>%s
	                                                </td>
	                                                </tr>
	                                                <tr>
	                                                <td>
	                                                    <p class='cacao'>Тип матраса
	                                                </td>
	                                                <td>
	                                                    <p class='text-end'>%s
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
	                                                    <p class='text-end'>%s
	                                                </td>
	                                            </tr>
	                                            <tr>
	                                                <td>
	                                                    <p class='cacao'>Стиль дизайна
	                                                </td>
	                                                <td>
	                                                    <p class='text-end'>%s
	                                                </td>
	                                            </tr>
	                                            <tr>
	                                                <td>
	                                                    <p class='cacao'>Материал наполнителя
	                                                </td>
	                                                <td>
	                                                    <p class='text-end'>%s
	                                                </td>
	                                            </tr>
	                                        </table>
	                                    </div>
	                                    <p>Конструктивные особенности: %s
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
	                                        <p>%s
	                                    </div>
	                                    <div class='col-md-4 col-sm-12'>
	                                        <img src='%s' class='img-fluid'>
	                                    </div>
	                                </div>
	                                <p>Больше образцов тканей вы можете посмотреть в наших салонах.
	                                    <a href='http://temp.decona.ru/showrooms/'><button class='btn-outline-gray'>Адреса салонов</button></a>
	                            </div>
	                        </div>
	                    </div>
	                </div>


	                <div class='accordion-item'><!-- Варианты исполнения ножек -->
	                    <h2 class='accordion-header' id='headingFive'>
	                        <button class='accordion-button' type='button' data-bs-toggle='collapse' data-bs-target='#collapseFive' aria-expanded='true' aria-controls='collapseFive'>
	                        Варианты исполнения ножек
	                        </button>
	                    </h2>
	                    <div id='collapseFive' class='accordion-collapse collapse' aria-labelledby='headingFive' data-bs-parent='#accordionExample'>
	                        <div class='accordion-body'>
	                            <div class='container-fluid'>
	                                <p>Массив дуба - природный материал в неповторимым рисунком
	                                <p class='cacao small-text'>В вашем изделии узор будет уникальным и может отличаться отпредставленных
	                            </div>
	                            <div class='container-fluid'>
	                                <div class='row'>
	                                    <div class='col-md-3 col-sm-6'>
	                                        <p class='major-text'>Sand</p>
	                                        <img src='http://temp.decona.ru/wp-content/uploads/2023/02/Leg_sand.png' class='card-img-top' alt='...'>
	                                    </div>
	                                    <div class='col-md-3 col-sm-6'>
	                                        <p class='major-text'>Black</p>
	                                        <img src='http://temp.decona.ru/wp-content/uploads/2023/02/Leg_Black.png' class='card-img-top' alt='...'>                 
	                                    </div>
	                                    <div class='col-md-3 col-sm-6'>
	                                        <p class='major-text'>Brandy</p>
	                                        <img src='http://temp.decona.ru/wp-content/uploads/2023/02/Leg_Brandy.png' class='card-img-top' alt='...'>
	                                    </div>
	                                    <div class='col-md-3 col-sm-6'>
	                                        <p class='major-text'>Arctic</p>
	                                        <img src='http://temp.decona.ru/wp-content/uploads/2023/02/Leg_Arctik.png' class='card-img-top' alt='...'>
	                                    </div>
	                                </div>
	                            </div>
	                        </div>
	                    </div>
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
	                                <p>Вы можете заказать как диван с декоративными утяжками на сидении, 
	                                <p>приспинных подушках и подлокотниках, так и без них
	                                </p>
	                            </div>
	                            <div class='container-fluid'>
	                                <div class='row'>
	                                    <div class='ps-5 col-md-6 col-sm-12'>
	                                        <p>С утяжками
	                                        <img src='http://temp.decona.ru/wp-content/uploads/2023/02/Seat_WOs-4.png'>
	                                    </div>
	                                    <div class='pe-5 col-md-6 col-sm-12'>
	                                        <p>Без утяжек
	                                        <img src='http://temp.decona.ru/wp-content/uploads/2023/02/Seat_WOs-4.png'>
	                                    </div>
	                                </div>
	                            </div>
	                        </div>
	                    </div>
	                </div>
	            </div>
	        </div>
	        <!-- the end of accordion part -->

	        <!-- Slider with interiors -->
	        <div class='mt-5 banner'>
	            <div id='carouselExampleIndicators' class='carousel slide' data-bs-ride='carousel'>
	                <div class='carousel-indicators'>
	                    <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='0' class='carousel-btn-bottom active' aria-current='true' aria-label='Slide 1'></button>
	                    <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='1' class='carousel-btn-bottom' aria-label='Slide 2'></button>
	                    <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='2' class='carousel-btn-bottom' aria-label='Slide 3'></button>
	                     <button type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide-to='3' class='carousel-btn-bottom' aria-label='Slide 4'></button>
	                </div>

	                <div class='carousel-inner' onmousemove='showPopOvers();'>
	                    <div class='carousel-item active'>
	                      <img src='http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_INTERIORS/CONSONO_1.jpg' class='d-block w-100' alt='...'>
	                    </div>
	                    <div class='carousel-item'>
	                      <img src='http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_INTERIORS/CONSONO_2.jpg' alt='...'>
	                    </div>
	                    <div class='carousel-item'>
	                      <img src='http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_INTERIORS/CONSONO_3.jpg' alt='...'>
	                    </div>
	                    <div class='carousel-item'>
	                      <img src='http://temp.decona.ru/wp-content/uploads/goods_pics/COLLECTIONS/CONSONO/CONSONO_INTERIORS/CONSONO_4.jpg' alt='...'>
	                    </div>
	                </div>

	                 <button class='carousel-control-prev' type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide='prev'>
	                    <span class='carousel-control-prev-icon pt-5' aria-hidden='true'></span>
	                    <span class='visually-hidden'>Previous</span>
	                  </button>
	                  <button class='carousel-control-next' type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide='next'>
	                    <span class='carousel-control-next-icon pt-5' aria-hidden='true'></span>
	                    <span class='visually-hidden'>Next</span>
	                  </button>
	            </div>  
	        </div>
	        <!-- Slider end -->

	        <!-- DESCTOP POP OVER THING START -->
	        <div class='popOverBlock pt-5 d-none d-lg-block d-xl-block d-xxl-block'>
	            <canvas id='canvasBig' style='display:block' width='1600' height='800'></canvas>

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
	        <div class='container-fluid big-fields-content mt-4'>
	            <p> Стоимость дивана в нестандартной комплектации рассчитывается в салоне, после выбора клиентом обивки и дополнительных опций. После того, как вы определилисть, подписывается договор, гле прописаны все особенности товара, его доставка и гарантии.</p>
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
	    </div>

	    <?php
	    get_footer();
	    ";
	$dir = 'http://temp.decona.ru/wp-content/uploads/catalog/goods-pages';

	print_r($template);
	

	while ($row = mysqli_fetch_assoc($result)) {
	    $sku = $row['sku'];
	    $collection = $row['collection'];
	    $category = $row['category'];
	    $category_ru = $row['category_ru'];
	    $model = $row['model'];
	    $fabric_type = $row['fabric_type'];
	    $fabric_name = $row['fabric_name'];
	    $product_img = $row['product_img'];
	    $product_img_mob = $row['product_img_mob'];
	    $is_new = $row['is_new'];
	    $available_for_delivery_2 = $row['available_for_delivery_2'];
	    $available_for_delivery_28 = $row['available_for_delivery_28'];
	    $available_in_showroom = $row['available_in_showroom'];
	    $carousel_item_1 = $row['carousel_item_1'];
	    $carousel_item_2 = $row['carousel_item_2'];
	    $carousel_item_3 = $row['carousel_item_3'];
	    $carousel_item_4 = $row['carousel_item_4'];
	    $carousel_item_5 = $row['carousel_item_5'];
	    $carousel_item_1_mob = $row['carousel_item_1_mob'];
	    $carousel_item_2_mob = $row['carousel_item_2_mob'];
	    $carousel_item_3_mob = $row['carousel_item_3_mob'];
	    $carousel_item_4_mob = $row['carousel_item_4_mob'];
	    $carousel_item_5_mob = $row['carousel_item_5_mob'];
	    $right_sofa_piece = $row['right_sofa_piece'];
	    $product_full_name = $row['product_full_name'];
	    $price = $row['price'];
	    $price_sale = $row['price_sale'];
	    $description = $row['description'];
	    $prod_width = $row['prod_width'];
	    $prod_depth = $row['prod_depth'];
	    $prod_height = $row['prod_height'];
	    $prod_weight = $row['prod_weight'];
	    $prod_seat_height = $row['prod_seat_height'];
	    $prod_seat_width = $row['prod_seat_width'];
	    $prod_seat_depth = $row['prod_seat_depth'];
	    $prod_back_width = $row['prod_back_width'];
	    $product_type = $row['product_type'];
	    $transform_type = $row['transform_type'];
	    $matress_type = $row['matress_type'];
	    $product_form = $row['product_form'];
	    $product_style = $row['product_style'];
	    $product_inside = $row['product_inside'];
	    $features = $row['features'];
	    $product_fabric_about = $row['product_fabric_about'];
	    $product_fabric_img = $row['product_fabric_img'];

	    $filename = $sku . '.php';
	    $content = sprintf($template, $sku, $product_name, $fabric_name, $model, $model, $model, $model, $model, $is_new, $available_in_showroom, $available_for_delivery_2, $carousel_item_1, $carousel_item_2, $carousel_item_3, $carousel_item_4, $carousel_item_5, $right_sofa_piece, $fabric_name, $model, $model, $model, $model, $model, $is_new, $available_in_showroom, $available_for_delivery_2, $carousel_item_1_mob, $carousel_item_2_mob, $carousel_item_3_mob, $carousel_item_4_mob, $carousel_item_5_mob, $product_full_name, $price_sale, $price, $product_full_name, $price_sale, $price, $description, $prod_width, $prod_depth, $prod_height, $prod_weight, $prod_seat_height, $prod_seat_width, $prod_seat_depth, $prod_back_width, $product_type, $transform_type, $matress_type, $product_form, $product_style, $product_inside, $features, $product_fabric_about, $product_fabric_img, $description, $prod_width, $prod_depth, $prod_height, $prod_weight, $prod_seat_height, $prod_seat_width, $prod_seat_depth, $prod_back_width, $product_type, $transform_type, $matress_type, $product_form, $product_style, $product_inside, $features, $product_fabric_about, $product_fabric_img);
	    file_put_contents($filename, $content);


	    print_r($sku);
		print_r($dir);
		
	}

	// Step 4: Display success message or log errors
	if ($result) {
	    echo 'Pages created successfully!';
	} else {
	    error_log('Error creating pages: ' . mysqli_error($conn));
	}

	// Step 5: Close the database connection
	mysqli_close($conn);
}

