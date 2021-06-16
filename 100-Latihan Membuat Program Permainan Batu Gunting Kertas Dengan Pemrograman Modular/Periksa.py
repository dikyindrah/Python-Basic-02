def periksa_pilihan_user(pilihan, pilihan_user):
    pilihan_user_ada = False

    for item in pilihan:
        if pilihan_user == item:
            pilihan_user_ada = True

    return pilihan_user_ada