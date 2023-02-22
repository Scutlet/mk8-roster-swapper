from dataclasses import dataclass
from enum import Enum


class MK8Character(Enum):
    INVALID = -1
    MARIO = 0x00
    LUIGI = 0x01
    PEACH = 0X02
    DAISY = 0x03
    YOSHI = 0x04
    TOAD = 0x05
    TOADETTE = 0x06
    KOOPA_TROOPA = 0x07
    BOWSER = 0x08
    DONKEY_KONG = 0x09
    WARIO = 0x0a
    WALUIGI = 0x0b
    ROSALINA = 0x0c
    METAL_MARIO = 0x0d
    PINK_GOLD_PEACH = 0x0e
    LAKITU = 0x0f
    SHY_GUY = 0x10
    BABY_MARIO = 0x11
    BABY_LUIGI = 0x12
    BABY_PEACH = 0x13
    BABY_DAISY = 0x14
    BABY_ROSALINA = 0x15
    LARRY = 0x16
    LEMMY = 0x17
    WENDY = 0x18
    LUDWIG = 0x19
    IGGY = 0x1a
    ROY = 0x1b
    MORTON = 0x1c
    MII = 0x1d
    TANOOKI_MARIO = 0x1e
    LINK = 0x1f
    VILLAGER_MALE = 0x20
    ISABELLE = 0x21
    CAT_PEACH = 0x22
    DRY_BOWSER = 0x23
    VILLAGER_FEMALE = 0x24

@dataclass
class SlotOffset:
    address: int
    register: int

    def generate_instruction(self, character: MK8Character) -> str:
        instruction = f"{self.address:#x} = li r{self.register}, {character.value:#x}"
        return f"{instruction:<24} # {character.name}"

SLOT_OFFSETS = (
    SlotOffset(0x025d6480, 6), # Mario
    SlotOffset(0x025d6450, 8), # Luigi
    SlotOffset(0x025d6448, 10), # Peach
    SlotOffset(0x025d64a8, 11), # Daisy
    SlotOffset(0x025d6490, 12), # Rosalina
    SlotOffset(0x025d6478, 4), # Metal Mario
    SlotOffset(0x025d64b0, 0), # Yoshi
    SlotOffset(0x025d6488, 5), # Toad
    SlotOffset(0x025d6498, 6), # Koopa Troopa
    SlotOffset(0x025d644c, 7), # Shy Guy
    SlotOffset(0x025d645c, 8), # Lakitu
    SlotOffset(0x025d6470, 9), # Toadette
    SlotOffset(0x025d6468, 10), # Baby Mario
    SlotOffset(0x025d64b8, 11), # Baby Luigi
    SlotOffset(0x025d64cc, 12), # Baby Peach
    SlotOffset(0x025d64c8, 4), # Baby Daisy
    SlotOffset(0x025d6540, 5), # Baby Rosalina
    SlotOffset(0x025d64e4, 6), # Pink Gold Peach
    SlotOffset(0x025d64ec, 7), # Bowser
    SlotOffset(0x025d64fc, 8), # Donkey Kong
    SlotOffset(0x025d64c0, 0), # Wario
    SlotOffset(0x025d64a0, 9), # Waluigi
    SlotOffset(0x025d64d4, 10), # Iggy
    SlotOffset(0x025d64dc, 11), # Roy
    SlotOffset(0x025d6504, 0), # Lemmy
    SlotOffset(0x025d6528, 12), # Larry
    SlotOffset(0x025d6518, 4), # Wendy
    SlotOffset(0x025d6558, 5), # Ludwig
    SlotOffset(0x025d64f4, 6), # Morton
    SlotOffset(0x025d6538, 0), # Mii
    SlotOffset(0x025d650c, 7), # Tanooki Mario
    SlotOffset(0x025d6520, 8), # Cat Peach
    SlotOffset(0x025d6530, 9), # Link
    SlotOffset(0x025d6550, 10), # Male Villager (and Female Villager)
    SlotOffset(0x025d6560, 0), # Isabelle
    SlotOffset(0x025d6548, 11), # Dry Bowser
    # Female Villager doesn't have a separate slot, and automatically gets added to male villager's slot.
    #   The same goes for the Mii/Amiibo selection, and the Yoshi and Shy Guy
    #   color variants (which are character variants in the game-code)
)
