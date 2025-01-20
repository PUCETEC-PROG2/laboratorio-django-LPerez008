from django.urls import path
from . import views


app_name = 'pokedex' #Parte importante para poder traabajar con formularios.

urlpatterns = [
    #LISTADO DE POKEMOS Y TRAINERS
    path("", views.index, name="index"), #Pantalla de Pokemons
    path("trainers/", views.trainers, name="trainers"), #Pantalla de Pokemons

    #VISTA DE POKEMON O TRAINER INDIVIDUAL
    path("<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("trainers/<int:trainer_id>/", views.trainer_detail, name="trainer_detail"),

    #AÑADIR POKEMON O TRAINER
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"), #Añadir nuevo path
    path("add_trainer/", views.add_trainer, name="add_trainer"),

    #EDITAR POKEMON O TRAINER
    path("edit_pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
    path("trainers/edit_trainer/<int:trainer_id>/", views.edit_trainer, name="edit_trainer"),

    #Eliminar POKEMON O TRAINER
    path("delete_pokemon/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),
    path("trainers/delete_trainer/<int:trainer_id>/", views.delete_trainer, name="delete_trainer"),

    path("login/", views.CustomLoginView.as_view(), name = "login" )
]
