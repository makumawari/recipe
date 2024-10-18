from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    servings = models.CharField(max_length=50)
    instructions = models.TextField()
    cuisine = models.CharField(max_length=100)
    cooking_time = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.title

class Image(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="images")
    url = models.CharField(max_length=2083)
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.recipe.title}"

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RecipeTag(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('recipe', 'tag')

    def __str__(self):
        return f"{self.recipe.title} - {self.tag.name}"
