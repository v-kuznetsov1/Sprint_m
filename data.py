
class TestData:

    EMAIL_ALREADY_USE = 'Почта уже используется'
    NO_UPDATING_RIGHTS = "Оффер не найден или у вас нет прав на его редактирование"
    DELETE_MESSAGE = "Объявление удалено успешно"

    
    CREATE_LISTING_RESPONSE = ["id", "name", "category", "condition", "city", "description",
                               "price", "owner", "updatedAt", "createdAt", "img1", "img2", "img3", "isFavorite"
                               ]
    

    UPDATE_OFFER_RESPONSE = [   "id", "price", "name", "category", "condition", "city", "description",
                             "img1", "img2", "img3", "isFavorite", "owner", "createdAt", "updatedAt"
                             ]
