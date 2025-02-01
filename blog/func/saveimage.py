
def user_profile_image_path(instance, filename):
    """Stores profile images in a folder named after the user's email."""
    return f'media/{instance.email}/{filename}'