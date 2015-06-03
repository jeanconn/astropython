"""
This script registers the models with the Moderation app
"""

from moderation import moderation
from .models import Package

moderation.register(Package)