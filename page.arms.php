<?php
/*
Template name: arms
*/

get_header('new'); 
?>

<div class='thin ms-4'>
	<a href='http://temp.decona.ru/'>Главная</a> / <a href='http://temp.decona.ru/products/'>Продукция</a> / <a href='http://temp.decona.ru/#'>Кресла</a>
</div>
<p class="ms-4 my-2 major-text">Кресла</p>


	<?php
		
		//connection
		$conn = mysqli_connect("localhost", "deconaru", "WULk_JT76BF7KULL", "deconaru");
		//render arms
		$query = "SELECT * FROM goods_woder WHERE category = 'arm'";
		$result = mysqli_query($conn, $query);	
		
		while ($row = mysqli_fetch_array($result)) {
		echo "
		<div class='products_container' id='products_container'>
		    <div class = 'product_card sku m-2 p-4' id='" . $row['sku'] . "' onclick='createNewPageOnClick('" . $row['sku'] . "')'>
	    		<div class = 'd-flex justify-content-between'>
					<h3 class='product_card_header'>" . $row[product_name] . "</h3>
					<div>
						<img class = 'is_new_icon' src='" . $row[is_new] . "'>
						<img class = 'available_icon' src='" . $row[available_in_showroom] . "'> 
						<img class = 'available_icon'src='" . $row[available_for_delivery_2] . "'>
					</div>
				</div>

				<center>
					<img src='" . $row[product_img] . "' class='img-fluid product_img_under'>
				</center>
				
				<div class = 'd-flex justify-content-between'>
					<div class='cacao'>В наличии</div>
					<div class='old-price_cat_page'>" . $row[price] . " ₽</div>
				</div>

				<div class = 'd-flex justify-content-between'>
					<div class='cacao'>" . $row[prod_width] . "×" . $row[prod_depth] . "×" . $row[prod_height] . "</div>
					<div class='cacao price_cat_page'>" . $row[price_sale] . " ₽</div>
				</div>
				
			</div>
		</div>";
		}
		
		mysql_close();
	?>
	

<?php
get_footer();