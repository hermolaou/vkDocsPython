from services.vk_service import VkService

class BusinessLogic:
    def __init__(self, token):
        self.vk_service = VkService()
        self.token = token

    def search_doc(self, search, limit, offset, own_docs=True):
        return self.vk_service.search_docs(search, limit, offset, own_docs, self.token)
