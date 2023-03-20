from Repository.repository import Repository


class ClientRepository(Repository):
    
    def __init__(self):
        super().__init__()

    def get_client_name(self, id_client):
        """Functia prin care se preia numele unui client

        :param id_client: id-ul clientului pentru care se va returna numele
        :return: numele clientului
        """
        for i in range(0, len(self._lista)):
            current_client = self._lista[i]
            if current_client.get_id() == id_client:
                return current_client.getName()
        return None
  