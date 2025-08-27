from rest_framework import serializers
from .models import Listing, Booking, Review
from django.contrib.auth.models import User


class UserSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'booking', 'rating', 'comment', 'created_at')
        read_only_fields = ('id', 'created_at')


class BookingSerializer(serializers.ModelSerializer):
    user = UserSummarySerializer(read_only=True)
    review = ReviewSerializer(read_only=True)


class Meta:
    model = Booking
    fields = ('id', 'listing', 'user', 'start_date', 'end_date', 'created_at', 'review')
    read_only_fields = ('id', 'created_at')


class ListingSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)
    reviews = serializers.SerializerMethodField()


class Meta:
    model = Listing
    fields = ('id', 'title', 'description', 'price_per_night', 'location', 'created_at', 'bookings', 'reviews')
    read_only_fields = ('id', 'created_at', 'bookings', 'reviews')


def get_reviews(self, obj):
    # return aggregated review data or serialized reviews
    qs = obj.reviews.select_related('booking')
    return ReviewSerializer(qs, many=True).data