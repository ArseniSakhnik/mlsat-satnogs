from typing import Union


class NoradInfo:
    def __init__(self, temporary_norad_id: int, followed_norad_id: int):
        self.temporary_norad_id = temporary_norad_id
        self.followed_norad_id = followed_norad_id


class BasicDecoder:
    def __init__(self, decoder_title: str, satellite_id: str, norad_id: Union[int, NoradInfo]):
        self.decoder_title = decoder_title
        self.satellite_id = satellite_id
        self.norad_id = norad_id
