class Product(models.Model):
	collection = models.ForeignKey(Collection,
		on_delete=models.CASCADE)
	fabric_name = models.ForeignKey(Fabric,on_delete=models.CASCADE)
	price = models.IntegerField(blank=True,null=True)
	width = models.IntegerField(blank=True, null=True)
	depth = models.IntegerField(blank=True, null=True)
	paws_type = models.CharField(max_length=50, null=True, blank=True)
	mechanism_type = models.CharField(max_length=50, null=True, blank=True)
	linen_drawer = models.CharField(max_length=50, null=True, blank=True)

	@property
	def fabric_color(self):
		return self.fabric_name.product_fabric_color
	@property
	def type_id(self):
		return self.category.type_id