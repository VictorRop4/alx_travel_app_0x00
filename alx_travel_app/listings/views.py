from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Listing, Booking, Review
from .serializers import ListingSerializer, BookingSerializer, ReviewSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related('listing', 'user').all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


def perform_create(self, serializer):
    # attach current user as the booking user
    serializer.save(user=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related('booking', 'booking__user', 'booking__listing').all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def create(self, request, *args, **kwargs):
    # ensure review is created only if booking exists and belongs to user (optional rule)
    return super().create(request, *args, **kwargs)