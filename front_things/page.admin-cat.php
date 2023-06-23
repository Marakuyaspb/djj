<?php
/*
Template name: admin-cat
*/
get_header('new'); 


if(isset($_POST['create_prod_pages'])){
	// Step 1: Connect to the MySQL database
	
	$conn = mysqli_connect("localhost", "deconaru", "WULk_JT76BF7KULL", "deconaru");

	// Check connection
	if (!$conn) {
		print_r('Sorry. Connection failed');
	    die('Connection failed: ' . mysqli_connect_error());

	}

	// Step 2: Fetch data from the database
	$sql = 'SELECT * FROM g_t';
	$result = mysqli_query($conn, $sql);

	// Create new HTML pages
	$template = "
	    <?php
	    get_header('new'); 
	    ?>
	    <div class='ms-4'>
		    <h3>%s</h3>
		    <h1>%s</h1>
		    <p>%s</p>
		    <img src='%s'>
		    <hr>
		    <img src='%s'>
		    <hr>
		    <p>%s</p>
	    </div>

	    <?php
	    get_footer();
	";
	$dir = 'http://temp.decona.ru/wp-content/uploads/catalog/goods-pages';

	while ($row = mysqli_fetch_assoc($result)) {
	    $sku = $row['sku'];
	    $product_name = $row['product name'];
	    $price = $row['price'];
	    $carousel_item_1 = $row['carousel_item_1'];
	    $carousel_item_1_mob = $row['carousel_item_1_mob'];
	    
	    print_r($sku . '<br>');
	    $filename = $sku . '.php';
	    $file_path = "http://temp.decona.ru/wp-content/uploads/catalog/goods-pages/$filename.php";

	    // open the file for writing
		//$file = fopen($file_path, "w");
		$file = fopen('file_path.php', "w");

	    $content = sprintf($template, $sku, $product_name, $price, $carousel_item_1, $carousel_item_1_mob, $price);

	    fwrite($filename, $content);
	    fclose($file);

	    //print_r($price . '<br>');		
	}

	// Display success message or log errors
	if ($result) {
	    echo 'Pages created successfully!';
	} else {
	    error_log('Error creating pages: ' . mysqli_error($conn));
	}

	// Step 5: Close the database connection
	mysqli_close($conn);
}


?>

<div class='container-fluid mt-2 ms-4'>
	<div class='row'>
		<div class='col'>
			<h3 class='mt-4'>Обновление данных</h3>
			<p>В базе данных phpMyAdmin обновлены данные об уже существующих товарах? Чтобы обновить отображение товаров на сайте, нажмите на кнопку ниже.</p>
			<form method="post">
				<button type='submit' class='btn btn-danger' name='update_prod_pages'>Обновить всё сущее</button>
			</form>
			<br>
			<hr>
			<h3 class='mt-2'>Создание страниц отдельных товаров</h3>
			<p>В базу данных phpMyAdmin добавлены новые товары? Чтобы создать страницы новых товаров, нажмите на кнопку ниже.</p>
			<form method="post">
				<button type='submit' class='btn btn-danger' name='create_prod_pages' style='background: red!important;'>Создать много новых страниц</button>
			</form>
		</div>

		<div class='col'>
			<img class='mt-3' src='http://temp.decona.ru/wp-content/uploads/2023/04/simons-cat.jpg'>
		</div>
	</div>
</div>



<?php
get_footer();