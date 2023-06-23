<?php
/**
 * Displays the post header
 *
 */

// Don't show the title if the post-format is `aside` or `status`.
$post_format = get_post_format();
if ( 'aside' === $post_format || 'status' === $post_format ) {
	return;
}
?>

<header class="entry-header">
	<hr>
		
	<?php
	the_title( sprintf( '<h3 class="entry-title default-max-width"><a href="%s">', esc_url( get_permalink() ) ), '</a></h3>' );
	twenty_twenty_one_post_thumbnail();
	?>
</header><!-- .entry-header -->

