# Models, Serializers, and Seeders

This section of the project covers the definition of core models, preparation of serializers for API representation, and database seeding for testing and development.

---

## Models

The project defines three primary models: `Listing`, `Booking`, and `Review`.

### Listing
Represents a property listing in the system.

```python
class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} — {self.location}"
