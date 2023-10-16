from .models import Profile

def num_matches(request):
    # Calculate the number of matches as needed
    current_user = Profile.objects.latest('id')
    users = Profile.objects.exclude(id=current_user.id)

    matching_users = []

    for user in users:
        if (
            user.budget - 500 <= current_user.budget <= user.budget + 500
            and user.currentL == current_user.currentL
            # and user.age == current_user.age
            # and abs(user.age - current_user.age) <= 5
        ):
            matching_users.append(user)

        elif user.smoking == current_user.smoking:
            matching_users.append(user)

    num_matches = len(matching_users)

    # Return a dictionary with the context variable
    return {'num_matches': num_matches}
