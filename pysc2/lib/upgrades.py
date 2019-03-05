# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Define the static list of upgrades for SC2."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import enum


# pylint: disable=invalid-name
class Upgrades(enum.IntEnum):
  """The list of upgrades, as generated by bin/gen_data.py."""
  AdaptiveTalons = 293
  AdrenalGlands = 65
  AdvancedBallistics = 140
  AnabolicSynthesis = 88
  AnionPulseCrystals = 99
  Blink = 87
  Burrow = 64
  CentrificalHooks = 75
  Charge = 86
  ChitinousPlating = 4
  CloakingField = 20
  CombatShield = 16
  ConcussiveShells = 17
  CorvidReactor = 22
  CycloneRapidFireLaunchers = 291
  DrillingClaws = 122
  ExtendedThermalLance = 50
  GlialReconstitution = 2
  GraviticBooster = 48
  GraviticDrive = 49
  GravitonCatapult = 1
  GroovedSpines = 134
  HiSecAutoTracking = 5
  HighCapacityFuelTanks = 139
  HyperflightRotors = 136
  InfernalPreigniter = 19
  LockOn = 144
  MetabolicBoost = 66
  MuscularAugments = 135
  NeosteelFrame = 10
  NeuralParasite = 101
  PathogenGlands = 74
  PersonalCloaking = 25
  PneumatizedCarapace = 62
  ProtossAirArmorsLevel1 = 81
  ProtossAirArmorsLevel2 = 82
  ProtossAirArmorsLevel3 = 83
  ProtossAirWeaponsLevel1 = 78
  ProtossAirWeaponsLevel2 = 79
  ProtossAirWeaponsLevel3 = 80
  ProtossGroundArmorsLevel1 = 42
  ProtossGroundArmorsLevel2 = 43
  ProtossGroundArmorsLevel3 = 44
  ProtossGroundWeaponsLevel1 = 39
  ProtossGroundWeaponsLevel2 = 40
  ProtossGroundWeaponsLevel3 = 41
  ProtossShieldsLevel1 = 45
  ProtossShieldsLevel2 = 46
  ProtossShieldsLevel3 = 47
  PsiStorm = 52
  ResonatingGlaives = 130
  ShadowStrike = 141
  SmartServos = 289
  Stimpack = 15
  TerranInfantryArmorsLevel1 = 11
  TerranInfantryArmorsLevel2 = 12
  TerranInfantryArmorsLevel3 = 13
  TerranInfantryWeaponsLevel1 = 7
  TerranInfantryWeaponsLevel2 = 8
  TerranInfantryWeaponsLevel3 = 9
  TerranShipWeaponsLevel1 = 36
  TerranShipWeaponsLevel2 = 37
  TerranShipWeaponsLevel3 = 38
  TerranStructureArmor = 6
  TerranVehicleAndShipArmorsLevel1 = 116
  TerranVehicleAndShipArmorsLevel2 = 117
  TerranVehicleAndShipArmorsLevel3 = 118
  TerranVehicleWeaponsLevel1 = 30
  TerranVehicleWeaponsLevel2 = 31
  TerranVehicleWeaponsLevel3 = 32
  TunnelingClaws = 3
  WarpGateResearch = 84
  WeaponRefit = 76
  ZergFlyerArmorsLevel1 = 71
  ZergFlyerArmorsLevel2 = 72
  ZergFlyerArmorsLevel3 = 73
  ZergFlyerWeaponsLevel1 = 68
  ZergFlyerWeaponsLevel2 = 69
  ZergFlyerWeaponsLevel3 = 70
  ZergGroundArmorsLevel1 = 56
  ZergGroundArmorsLevel2 = 57
  ZergGroundArmorsLevel3 = 58
  ZergMeleeWeaponsLevel1 = 53
  ZergMeleeWeaponsLevel2 = 54
  ZergMeleeWeaponsLevel3 = 55
  ZergMissileWeaponsLevel1 = 59
  ZergMissileWeaponsLevel2 = 60
  ZergMissileWeaponsLevel3 = 61