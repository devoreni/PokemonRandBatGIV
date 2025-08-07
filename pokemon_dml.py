from BTrees.OOBTree import OOBTree
import ZODB, ZODB.FileStorage
import persistent
import pokemon_ddl
import transaction


def runDML():
    storage = ZODB.FileStorage.FileStorage('PokeData.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root

    if not hasattr(root, 'moves'):
        root.moves = OOBTree()
    if not hasattr(root, 'pokesets'):
        root.pokesets = OOBTree()

    if 'Physical Moves':
        # Normal-type moves
        root.moves['Barrage'] = pokemon_ddl.Move('Barrage', 15, 0.85, 'Phys', 'Normal')
        root.moves['Bide'] = pokemon_ddl.Move('Bide', 0, 1.0, 'Phys', 'Normal')
        root.moves['Body Slam'] = pokemon_ddl.Move('Body Slam', 85, 1.0, 'Phys', 'Normal')
        root.moves['Comet Punch'] = pokemon_ddl.Move('Comet Punch', 18, .85, 'Phys', 'Normal')
        root.moves['Constrict'] = pokemon_ddl.Move('Constrict', 10, 1.0, 'Phys', 'Normal')
        root.moves['Covet'] = pokemon_ddl.Move('Covet', 40, 1.0, 'Phys', 'Normal')
        root.moves['Crush Claw'] = pokemon_ddl.Move('Crush Claw', 75, .95, 'Phys', 'Normal')
        root.moves['Crush Grip'] = pokemon_ddl.Move('Crush Grip', 0, 1.0, 'Phys', 'Normal')
        root.moves['Cut'] = pokemon_ddl.Move('Cut', 50, 0.95, 'Phys', 'Normal')
        root.moves['Double-edge'] = pokemon_ddl.Move('Double-edge', 120, 1.0, 'Phys', 'Normal')
        root.moves['Double Hit'] = pokemon_ddl.Move('Double Hit', 35, 0.9, 'Phys', 'Normal')
        root.moves['Doubleslap'] = pokemon_ddl.Move('Doubleslap', 15, 0.85, 'Phys', 'Normal')
        root.moves['Egg Bomb'] = pokemon_ddl.Move('Egg Bomb', 100, 0.75, 'Phys', 'Normal')
        root.moves['Endeavor'] = pokemon_ddl.Move('Endeavor', 0, 1.0, 'Phys', 'Normal')
        root.moves['Explosion'] = pokemon_ddl.Move('Explosion', 250, 1.0, 'Phys', 'Normal')
        root.moves['ExtremeSpeed'] = pokemon_ddl.Move('ExtremeSpeed', 80, 1.0, 'Phys', 'Normal')
        root.moves['Facade'] = pokemon_ddl.Move('Facade', 70, 1.0, 'Phys', 'Normal')
        root.moves['Fake Out'] = pokemon_ddl.Move('Fake Out', 40, 1.0, 'Phys', 'Normal')
        root.moves['False Swipe'] = pokemon_ddl.Move('False Swipe', 40, 1.0, 'Phys', 'Normal')
        root.moves['Flail'] = pokemon_ddl.Move('Flail', 0, 1.0, 'Phys', 'Normal')
        root.moves['Frustration'] = pokemon_ddl.Move('Frustration', 0, 1.0, 'Phys', 'Normal')
        root.moves['Fury Attack'] = pokemon_ddl.Move('Fury Attack', 15, 0.85, 'Phys', 'Normal')
        root.moves['Fury Swipes'] = pokemon_ddl.Move('Fury Swipes', 18, 0.8, 'Phys', 'Normal')
        root.moves['Giga Impact'] = pokemon_ddl.Move('Giga Impact', 150, 0.9, 'Phys', 'Normal')
        root.moves['Guillotine'] = pokemon_ddl.Move('Guillotine', 0, 0.3, 'Phys', 'Normal')
        root.moves['Headbutt'] = pokemon_ddl.Move('Headbutt', 70, 1.0, 'Phys', 'Normal')
        root.moves['Horn Attack'] = pokemon_ddl.Move('Horn Attack', 65, 1.0, 'Phys', 'Normal')
        root.moves['Horn Drill'] = pokemon_ddl.Move('Horn Drill', 0, 0.3, 'Phys', 'Normal')
        root.moves['Hyper Fang'] = pokemon_ddl.Move('Hyper Fang', 80, 0.9, 'Phys', 'Normal')
        root.moves['Last Resort'] = pokemon_ddl.Move('Last Resort', 130, 1.0, 'Phys', 'Normal')
        root.moves['Mega Kick'] = pokemon_ddl.Move('Mega Kick', 120, 0.75, 'Phys', 'Normal')
        root.moves['Mega Punch'] = pokemon_ddl.Move('Mega Punch', 80, 0.85, 'Phys', 'Normal')
        root.moves['Natural Gift'] = pokemon_ddl.Move('Natural Gift', 0, 1.0, 'Phys', 'Normal')
        root.moves['Pay Day'] = pokemon_ddl.Move('Pay Day', 40, 1.0, 'Phys', 'Normal')
        root.moves['Pound'] = pokemon_ddl.Move('Pound', 40, 1.0, 'Phys', 'Normal')
        root.moves['Present'] = pokemon_ddl.Move('Present', 0, 0.9, 'Phys', 'Normal')
        root.moves['Quick Attack'] = pokemon_ddl.Move('Quick Attack', 40, 1.0, 'Phys', 'Normal')
        root.moves['Rage'] = pokemon_ddl.Move('Rage', 20, 1.0, 'Phys', 'Normal')
        root.moves['Rapid Spin'] = pokemon_ddl.Move('Rapid Spin', 20, 1.0, 'Phys', 'Normal')
        root.moves['Return'] = pokemon_ddl.Move('Return', 0, 1.0, 'Phys', 'Normal')
        root.moves['Rock Climb'] = pokemon_ddl.Move('Rock Climb', 90, 0.85, 'Phys', 'Normal')
        root.moves['Scratch'] = pokemon_ddl.Move('Scratch', 40, 1.0, 'Phys', 'Normal')
        root.moves['Secret Power'] = pokemon_ddl.Move('Secret Power', 70, 1.0, 'Phys', 'Normal')
        root.moves['Selfdestruct'] = pokemon_ddl.Move('Selfdestruct', 200, 1.0, 'Phys', 'Normal')
        root.moves['Skull Bash'] = pokemon_ddl.Move('Skull Bash', 100, 1.0, 'Phys', 'Normal')
        root.moves['Slam'] = pokemon_ddl.Move('Slam', 80, 0.75, 'Phys', 'Normal')
        root.moves['Slash'] = pokemon_ddl.Move('Slash', 70, 1.0, 'Phys', 'Normal')
        root.moves['Smellingsalt'] = pokemon_ddl.Move('Smellingsalt', 60, 1, 'Phys', 'Normal')
        root.moves['Spike Cannon'] = pokemon_ddl.Move('Spike Cannon', 20, 1.0, 'Phys', 'Normal')
        root.moves['Stomp'] = pokemon_ddl.Move('Stomp', 65, 1.0, 'Phys', 'Normal')
        root.moves['Strength'] = pokemon_ddl.Move('Strength', 80, 1.0, 'Phys', 'Normal')
        root.moves['Struggle'] = pokemon_ddl.Move('Struggle', 50, 1.0, 'Phys', 'Normal')
        root.moves['Super Fang'] = pokemon_ddl.Move('Super Fang', 0, 0.9, 'Phys', 'Normal')
        root.moves['Tackle'] = pokemon_ddl.Move('Tackle', 35, 0.95, 'Phys', 'Normal')
        root.moves['Take Down'] = pokemon_ddl.Move('Take Down', 90, 0.85, 'Phys', 'Normal')
        root.moves['Thrash'] = pokemon_ddl.Move('Thrash', 90, 1.0, 'Phys', 'Normal')
        root.moves['Vicegrip'] = pokemon_ddl.Move('Vicegrip', 55, 1.0, 'Phys', 'Normal')
        root.moves['Wrap'] = pokemon_ddl.Move('Wrap', 15, 0.85, 'Phys', 'Normal')

        # Fighting-type moves
        root.moves['Arm Thrust'] = pokemon_ddl.Move('Arm Thrust', 15, 1.0, 'Phys', 'Fighting')
        root.moves['Brick Break'] = pokemon_ddl.Move('Brick Break', 75, 1.0, 'Phys', 'Fighting')
        root.moves['Close Combat'] = pokemon_ddl.Move('Close Combat', 120, 1.0, 'Phys', 'Fighting')
        root.moves['Counter'] = pokemon_ddl.Move('Counter', 0, 1.0, 'Phys', 'Fighting')
        root.moves['Cross Chop'] = pokemon_ddl.Move('Cross Chop', 100, 0.8, 'Phys', 'Fighting')
        root.moves['Double Kick'] = pokemon_ddl.Move('Double Kick', 30, 1.0, 'Phys', 'Fighting')
        root.moves['Drain Punch'] = pokemon_ddl.Move('Drain Punch', 60, 1.0, 'Phys', 'Fighting')
        root.moves['DynamicPunch'] = pokemon_ddl.Move('DynamicPunch', 100, 0.5, 'Phys', 'Fighting')
        root.moves['Focus Punch'] = pokemon_ddl.Move('Focus Punch', 150, 1.0, 'Phys', 'Fighting')
        root.moves['Force Palm'] = pokemon_ddl.Move('Force Palm', 60, 1.0, 'Phys', 'Fighting')
        root.moves['Hammer Arm'] = pokemon_ddl.Move('Hammer Arm', 100, 0.9, 'Phys', 'Fighting')
        root.moves['Hi Jump Kick'] = pokemon_ddl.Move('Hi Jump Kick', 100, 0.9, 'Phys', 'Fighting')
        root.moves['Jump Kick'] = pokemon_ddl.Move('Jump Kick', 85, 0.95, 'Phys', 'Fighting')
        root.moves['Karate Chop'] = pokemon_ddl.Move('Karate Chop', 50, 1.0, 'Phys', 'Fighting')
        root.moves['Low Kick'] = pokemon_ddl.Move('Low Kick', 0, 1.0, 'Phys', 'Fighting')
        root.moves['Mach Punch'] = pokemon_ddl.Move('Mach Punch', 40, 1.0, 'Phys', 'Fighting')
        root.moves['Revenge'] = pokemon_ddl.Move('Revenge', 60, 1.0, 'Phys', 'Fighting')
        root.moves['Reversal'] = pokemon_ddl.Move('Reversal', 0, 1.0, 'Phys', 'Fighting')
        root.moves['Rock Smash'] = pokemon_ddl.Move('Rock Smash', 40, 1.0, 'Phys', 'Fighting')
        root.moves['Rolling Kick'] = pokemon_ddl.Move('Rolling Kick', 60, 0.85, 'Phys', 'Fighting')
        root.moves['Seismic Toss'] = pokemon_ddl.Move('Seismic Toss', 0, 1.0, 'Phys', 'Fighting')
        root.moves['Sky Uppercut'] = pokemon_ddl.Move('Sky Uppercut', 85, 0.9, 'Phys', 'Fighting')
        root.moves['Submission'] = pokemon_ddl.Move('Submission', 80, 0.8, 'Phys', 'Fighting')
        root.moves['Superpower'] = pokemon_ddl.Move('Superpower', 120, 1.0, 'Phys', 'Fighting')
        root.moves['Triple Kick'] = pokemon_ddl.Move('Triple Kick', 10, 0.9, 'Phys', 'Fighting')
        root.moves['Vital Throw'] = pokemon_ddl.Move('Vital Throw', 70, 1.0, 'Phys', 'Fighting')
        root.moves['Wake-up Slap'] = pokemon_ddl.Move('Wake-up Slap', 60, 1.0, 'Phys', 'Fighting')

        # Flying-type moves
        root.moves['Aerial Ace'] = pokemon_ddl.Move('Aerial Ace', 60, 1.0, 'Phys', 'Flying')
        root.moves['Bounce'] = pokemon_ddl.Move('Bounce', 85, 0.85, 'Phys', 'Flying')
        root.moves['Brave Bird'] = pokemon_ddl.Move('Brave Bird', 120, 1.0, 'Phys', 'Flying')
        root.moves['Drill Peck'] = pokemon_ddl.Move('Drill Peck', 80, 1.0, 'Phys', 'Flying')
        root.moves['Fly'] = pokemon_ddl.Move('Fly', 90, 0.95, 'Phys', 'Flying')
        root.moves['Peck'] = pokemon_ddl.Move('Peck', 35, 1.0, 'Phys', 'Flying')
        root.moves['Pluck'] = pokemon_ddl.Move('Pluck', 60, 1.0, 'Phys', 'Flying')
        root.moves['Sky Attack'] = pokemon_ddl.Move('Sky Attack', 140, 0.9, 'Phys', 'Flying')
        root.moves['Wing Attack'] = pokemon_ddl.Move('Wing Attack', 60, 1.0, 'Phys', 'Flying')

        # Poison-type moves
        root.moves['Cross Poison'] = pokemon_ddl.Move('Cross Poison', 70, 1.0, 'Phys', 'Poison')
        root.moves['Gunk Shot'] = pokemon_ddl.Move('Gunk Shot', 120, 0.7, 'Phys', 'Poison')
        root.moves['Poison Fang'] = pokemon_ddl.Move('Poison Fang', 50, 1.0, 'Phys', 'Poison')
        root.moves['Poison Jab'] = pokemon_ddl.Move('Poison Jab', 80, 1.0, 'Phys', 'Poison')
        root.moves['Poison Sting'] = pokemon_ddl.Move('Poison Sting', 15, 1.0, 'Phys', 'Poison')
        root.moves['Poison Tail'] = pokemon_ddl.Move('Poison Tail', 50, 1.0, 'Phys', 'Poison')

        # Ground-type moves
        root.moves['Bone Club'] = pokemon_ddl.Move('Bone Club', 65, 0.85, 'Phys', 'Ground')
        root.moves['Bone Rush'] = pokemon_ddl.Move('Bone Rush', 25, 0.8, 'Phys', 'Ground')
        root.moves['Bonemerang'] = pokemon_ddl.Move('Bonemerang', 50, 0.9, 'Phys', 'Ground')
        root.moves['Dig'] = pokemon_ddl.Move('Dig', 80, 1.0, 'Phys', 'Ground')
        root.moves['Earthquake'] = pokemon_ddl.Move('Earthquake', 100, 1.0, 'Phys', 'Ground')
        root.moves['Fissure'] = pokemon_ddl.Move('Fissure', 0, 0.3, 'Phys', 'Ground')
        root.moves['Magnitude'] = pokemon_ddl.Move('Magnitude', 0, 1.0, 'Phys', 'Ground')
        root.moves['Sand Tomb'] = pokemon_ddl.Move('Sand Tomb', 15, 0.7, 'Phys', 'Ground')

        # Rock-type moves
        root.moves['Head Smash'] = pokemon_ddl.Move('Head Smash', 150, 0.8, 'Phys', 'Rock')
        root.moves['Rock Blast'] = pokemon_ddl.Move('Rock Blast', 25, 0.8, 'Phys', 'Rock')
        root.moves['Rock Slide'] = pokemon_ddl.Move('Rock Slide', 75, 0.9, 'Phys', 'Rock')
        root.moves['Rock Throw'] = pokemon_ddl.Move('Rock Throw', 50, 0.9, 'Phys', 'Rock')
        root.moves['Rock Tomb'] = pokemon_ddl.Move('Rock Tomb', 50, 0.8, 'Phys', 'Rock')
        root.moves['Rock Wrecker'] = pokemon_ddl.Move('Rock Wrecker', 150, 0.9, 'Phys', 'Rock')
        root.moves['Rollout'] = pokemon_ddl.Move('Rollout', 30, 0.9, 'Phys', 'Rock')
        root.moves['Stone Edge'] = pokemon_ddl.Move('Stone Edge', 100, 0.8, 'Phys', 'Rock')

        # Bug-type moves
        root.moves['Attack Order'] = pokemon_ddl.Move('Attack Order', 90, 1.0, 'Phys', 'Bug')
        root.moves['Bug Bite'] = pokemon_ddl.Move('Bug Bite', 60, 1.0, 'Phys', 'Bug')
        root.moves['Fury Cutter'] = pokemon_ddl.Move('Fury Cutter', 10, 0.95, 'Phys', 'Bug')
        root.moves['Leech Life'] = pokemon_ddl.Move('Leech Life', 20, 1.0, 'Phys', 'Bug')
        root.moves['Megahorn'] = pokemon_ddl.Move('Megahorn', 120, 0.85, 'Phys', 'Bug')
        root.moves['Pin Missile'] = pokemon_ddl.Move('Pin Missile', 14, 0.85, 'Phys', 'Bug')
        root.moves['Twineedle'] = pokemon_ddl.Move('Twineedle', 25, 1.0, 'Phys', 'Bug')
        root.moves['U-turn'] = pokemon_ddl.Move('U-turn', 70, 1.0, 'Phys', 'Bug')
        root.moves['X-Scissor'] = pokemon_ddl.Move('X-Scissor', 80, 1.0, 'Phys', 'Bug')

        # Ghost-type moves
        root.moves['Astonish'] = pokemon_ddl.Move('Astonish', 30, 1.0, 'Phys', 'Ghost')
        root.moves['Lick'] = pokemon_ddl.Move('Lick', 20, 1.0, 'Phys', 'Ghost')
        root.moves['Shadow Claw'] = pokemon_ddl.Move('Shadow Claw', 70, 1.0, 'Phys', 'Ghost')
        root.moves['Shadow Force'] = pokemon_ddl.Move('Shadow Force', 120, 1.0, 'Phys', 'Ghost')
        root.moves['Shadow Punch'] = pokemon_ddl.Move('Shadow Punch', 60, 1.0, 'Phys', 'Ghost')
        root.moves['Shadow Sneak'] = pokemon_ddl.Move('Shadow Sneak', 40, 1.0, 'Phys', 'Ghost')

        # Steel-type moves
        root.moves['Bullet Punch'] = pokemon_ddl.Move('Bullet Punch', 40, 1.0, 'Phys', 'Steel')
        root.moves['Gyro Ball'] = pokemon_ddl.Move('Gyro Ball', 0, 1.0, 'Phys', 'Steel')
        root.moves['Iron Head'] = pokemon_ddl.Move('Iron Head', 80, 1.0, 'Phys', 'Steel')
        root.moves['Iron Tail'] = pokemon_ddl.Move('Iron Tail', 100, 0.75, 'Phys', 'Steel')
        root.moves['Magnet Bomb'] = pokemon_ddl.Move('Magnet Bomb', 60, 1.0, 'Phys', 'Steel')
        root.moves['Metal Burst'] = pokemon_ddl.Move('Metal Burst', 0, 1.0, 'Phys', 'Steel')
        root.moves['Metal Claw'] = pokemon_ddl.Move('Metal Claw', 50, 0.95, 'Phys', 'Steel')
        root.moves['Meteor Mash'] = pokemon_ddl.Move('Meteor Mash', 100, 0.85, 'Phys', 'Steel')
        root.moves['Steel Wing'] = pokemon_ddl.Move('Steel Wing', 70, 0.9, 'Phys', 'Steel')

        # Fire-type moves
        root.moves['Blaze Kick'] = pokemon_ddl.Move('Blaze Kick', 85, 0.9, 'Phys', 'Fire')
        root.moves['Fire Fang'] = pokemon_ddl.Move('Fire Fang', 65, 0.95, 'Phys', 'Fire')
        root.moves['Fire Punch'] = pokemon_ddl.Move('Fire Punch', 75, 1.0, 'Phys', 'Fire')
        root.moves['Flame Wheel'] = pokemon_ddl.Move('Flame Wheel', 60, 1.0, 'Phys', 'Fire')
        root.moves['Flare Blitz'] = pokemon_ddl.Move('Flare Blitz', 120, 1.0, 'Phys', 'Fire')
        root.moves['Sacred Fire'] = pokemon_ddl.Move('Sacred Fire', 100, 0.95, 'Phys', 'Fire')

        # Water-type moves
        root.moves['Aqua Jet'] = pokemon_ddl.Move('Aqua Jet', 40, 1.0, 'Phys', 'Water')
        root.moves['Aqua Tail'] = pokemon_ddl.Move('Aqua Tail', 90, 0.9, 'Phys', 'Water')
        root.moves['Clamp'] = pokemon_ddl.Move('Clamp', 35, 0.75, 'Phys', 'Water')
        root.moves['Crabhammer'] = pokemon_ddl.Move('Crabhammer', 90, 0.85, 'Phys', 'Water')
        root.moves['Dive'] = pokemon_ddl.Move('Dive', 80, 1.0, 'Phys', 'Water')
        root.moves['Waterfall'] = pokemon_ddl.Move('Waterfall', 80, 1.0, 'Phys', 'Water')

        # Grass-type moves
        root.moves['Bullet Seed'] = pokemon_ddl.Move('Bullet Seed', 10, 1.0, 'Phys', 'Grass')
        root.moves['Leaf Blade'] = pokemon_ddl.Move('Leaf Blade', 90, 1.0, 'Phys', 'Grass')
        root.moves['Needle Arm'] = pokemon_ddl.Move('Needle Arm', 60, 1.0, 'Phys', 'Grass')
        root.moves['Power Whip'] = pokemon_ddl.Move('Power Whip', 120, 0.85, 'Phys', 'Grass')
        root.moves['Razor Leaf'] = pokemon_ddl.Move('Razor Leaf', 55, 0.95, 'Phys', 'Grass')
        root.moves['Seed Bomb'] = pokemon_ddl.Move('Seed Bomb', 80, 1.0, 'Phys', 'Grass')
        root.moves['Vine Whip'] = pokemon_ddl.Move('Vine Whip', 35, 1.0, 'Phys', 'Grass')
        root.moves['Wood Hammer'] = pokemon_ddl.Move('Wood Hammer', 120, 1.0, 'Phys', 'Grass')

        # Electric-type moves
        root.moves['Spark'] = pokemon_ddl.Move('Spark', 65, 1.0, 'Phys', 'Electric')
        root.moves['Thunder Fang'] = pokemon_ddl.Move('Thunder Fang', 65, 0.95, 'Phys', 'Electric')
        root.moves['ThunderPunch'] = pokemon_ddl.Move('ThunderPunch', 75, 1.0, 'Phys', 'Electric')
        root.moves['Volt Tackle'] = pokemon_ddl.Move('Volt Tackle', 120, 1.0, 'Phys', 'Electric')

        # Psychic-type moves
        root.moves['Dizzy Punch'] = pokemon_ddl.Move('Dizzy Punch', 70, 1.0, 'Phys', 'Psychic')
        root.moves['Psycho Cut'] = pokemon_ddl.Move('Psycho Cut', 70, 1.0, 'Phys', 'Psychic')
        root.moves['Zen Headbutt'] = pokemon_ddl.Move('Zen Headbutt', 80, 0.9, 'Phys', 'Psychic')

        # Ice-type moves
        root.moves['Avalanche'] = pokemon_ddl.Move('Avalanche', 60, 1.0, 'Phys', 'Ice')
        root.moves['Ice Ball'] = pokemon_ddl.Move('Ice Ball', 30, 0.9, 'Phys', 'Ice')
        root.moves['Ice Fang'] = pokemon_ddl.Move('Ice Fang', 65, 0.95, 'Phys', 'Ice')
        root.moves['Ice Punch'] = pokemon_ddl.Move('Ice Punch', 75, 1.0, 'Phys', 'Ice')
        root.moves['Ice Shard'] = pokemon_ddl.Move('Ice Shard', 40, 1.0, 'Phys', 'Ice')
        root.moves['Icicle Spear'] = pokemon_ddl.Move('Icicle Spear', 10, 1.0, 'Phys', 'Ice')

        # Dragon-type moves
        root.moves['Dragon Claw'] = pokemon_ddl.Move('Dragon Claw', 80, 1.0, 'Phys', 'Dragon')
        root.moves['Dragon Rush'] = pokemon_ddl.Move('Dragon Rush', 100, 0.75, 'Phys', 'Dragon')
        root.moves['Outrage'] = pokemon_ddl.Move('Outrage', 120, 1.0, 'Phys', 'Dragon')

        # Dark-type moves
        root.moves['Assurance'] = pokemon_ddl.Move('Assurance', 50, 1.0, 'Phys', 'Dark')
        root.moves['Beat Up'] = pokemon_ddl.Move('Beat Up', 10, 1.0, 'Phys', 'Dark')
        root.moves['Bite'] = pokemon_ddl.Move('Bite', 60, 1.0, 'Phys', 'Dark')
        root.moves['Crunch'] = pokemon_ddl.Move('Crunch', 80, 1.0, 'Phys', 'Dark')
        root.moves['Faint Attack'] = pokemon_ddl.Move('Faint Attack', 60, 1.0, 'Phys', 'Dark')
        root.moves['Feint'] = pokemon_ddl.Move('Feint', 50, 1.0, 'Phys', 'Dark')
        root.moves['Fling'] = pokemon_ddl.Move('Fling', 0, 1.0, 'Phys', 'Dark')
        root.moves['Knock Off'] = pokemon_ddl.Move('Knock Off', 20, 1.0, 'Phys', 'Dark')
        root.moves['Night Slash'] = pokemon_ddl.Move('Night Slash', 70, 1.0, 'Phys', 'Dark')
        root.moves['Payback'] = pokemon_ddl.Move('Payback', 50, 1.0, 'Phys', 'Dark')
        root.moves['Punishment'] = pokemon_ddl.Move('Punishment', 0, 1.0, 'Phys', 'Dark')
        root.moves['Pursuit'] = pokemon_ddl.Move('Pursuit', 40, 1.0, 'Phys', 'Dark')
        root.moves['Sucker Punch'] = pokemon_ddl.Move('Sucker Punch', 80, 1.0, 'Phys', 'Dark')
        root.moves['Thief'] = pokemon_ddl.Move('Thief', 40, 1.0, 'Phys', 'Dark')
    transaction.commit()

    if 'Special Moves':
        # Grass-type moves
        root.moves['Absorb'] = pokemon_ddl.Move('Absorb', 20, 1.0, 'Spec', 'Grass')
        root.moves['Energy Ball'] = pokemon_ddl.Move('Energy Ball', 80, 1.0, 'Spec', 'Grass')
        root.moves['Frenzy Plant'] = pokemon_ddl.Move('Frenzy Plant', 150, 0.9, 'Spec', 'Grass')
        root.moves['Giga Drain'] = pokemon_ddl.Move('Giga Drain', 60, 1.0, 'Spec', 'Grass')
        root.moves['Grass Knot'] = pokemon_ddl.Move('Grass Knot', 0, 1.0, 'Spec', 'Grass')
        root.moves['Leaf Storm'] = pokemon_ddl.Move('Leaf Storm', 140, 0.9, 'Spec', 'Grass')
        root.moves['Magical Leaf'] = pokemon_ddl.Move('Magical Leaf', 60, 1.0, 'Spec', 'Grass')
        root.moves['Mega Drain'] = pokemon_ddl.Move('Mega Drain', 40, 1.0, 'Spec', 'Grass')
        root.moves['Petal Dance'] = pokemon_ddl.Move('Petal Dance', 90, 1.0, 'Spec', 'Grass')
        root.moves['Seed Flare'] = pokemon_ddl.Move('Seed Flare', 120, 0.85, 'Spec', 'Grass')
        root.moves['SolarBeam'] = pokemon_ddl.Move('SolarBeam', 120, 1.0, 'Spec', 'Grass')

        # Poison-type moves
        root.moves['Acid'] = pokemon_ddl.Move('Acid', 40, 1.0, 'Spec', 'Poison')
        root.moves['Sludge'] = pokemon_ddl.Move('Sludge', 65, 1.0, 'Spec', 'Poison')
        root.moves['Sludge Bomb'] = pokemon_ddl.Move('Sludge Bomb', 90, 1.0, 'Spec', 'Poison')
        root.moves['Smog'] = pokemon_ddl.Move('Smog', 20, 0.7, 'Spec', 'Poison')

        # Flying-type moves
        root.moves['Aeroblast'] = pokemon_ddl.Move('Aeroblast', 100, 0.95, 'Spec', 'Flying')
        root.moves['Air Cutter'] = pokemon_ddl.Move('Air Cutter', 55, 0.95, 'Spec', 'Flying')
        root.moves['Air Slash'] = pokemon_ddl.Move('Air Slash', 75, 0.95, 'Spec', 'Flying')
        root.moves['Chatter'] = pokemon_ddl.Move('Chatter', 60, 1.0, 'Spec', 'Flying')
        root.moves['Gust'] = pokemon_ddl.Move('Gust', 40, 1.0, 'Spec', 'Flying')
        root.moves['Razor Wind'] = pokemon_ddl.Move('Razor Wind', 80, 1.0, 'Spec', 'Flying')

        # Rock-type moves
        root.moves['AncientPower'] = pokemon_ddl.Move('AncientPower', 60, 1.0, 'Spec', 'Rock')
        root.moves['Power Gem'] = pokemon_ddl.Move('Power Gem', 70, 1.0, 'Spec', 'Rock')

        # Fighting-type moves
        root.moves['Aura Sphere'] = pokemon_ddl.Move('Aura Sphere', 90, 1.0, 'Spec', 'Fighting')
        root.moves['Focus Blast'] = pokemon_ddl.Move('Focus Blast', 120, 0.7, 'Spec', 'Fighting')
        root.moves['Vacuum Wave'] = pokemon_ddl.Move('Vacuum Wave', 40, 1.0, 'Spec', 'Fighting')

        # Ice-type moves
        root.moves['Aurora Beam'] = pokemon_ddl.Move('Aurora Beam', 65, 1.0, 'Spec', 'Ice')
        root.moves['Blizzard'] = pokemon_ddl.Move('Blizzard', 120, 0.7, 'Spec', 'Ice')
        root.moves['Ice Beam'] = pokemon_ddl.Move('Ice Beam', 95, 1.0, 'Spec', 'Ice')
        root.moves['Icy Wind'] = pokemon_ddl.Move('Icy Wind', 55, 0.95, 'Spec', 'Ice')
        root.moves['Powder Snow'] = pokemon_ddl.Move('Powder Snow', 40, 1.0, 'Spec', 'Ice')
        root.moves['Sheer Cold'] = pokemon_ddl.Move('Sheer Cold', 0, 0.3, 'Spec', 'Ice')

        # Water-type moves
        root.moves['Brine'] = pokemon_ddl.Move('Brine', 65, 1.0, 'Spec', 'Water')
        root.moves['Bubble'] = pokemon_ddl.Move('Bubble', 20, 1.0, 'Spec', 'Water')
        root.moves['BubbleBeam'] = pokemon_ddl.Move('BubbleBeam', 65, 1.0, 'Spec', 'Water')
        root.moves['Hydro Cannon'] = pokemon_ddl.Move('Hydro Cannon', 150, 0.9, 'Spec', 'Water')
        root.moves['Hydro Pump'] = pokemon_ddl.Move('Hydro Pump', 120, 0.8, 'Spec', 'Water')
        root.moves['Muddy Water'] = pokemon_ddl.Move('Muddy Water', 95, 0.85, 'Spec', 'Water')
        root.moves['Octazooka'] = pokemon_ddl.Move('Octazooka', 65, 0.85, 'Spec', 'Water')
        root.moves['Surf'] = pokemon_ddl.Move('Surf', 95, 1.0, 'Spec', 'Water')
        root.moves['Water Gun'] = pokemon_ddl.Move('Water Gun', 40, 1.0, 'Spec', 'Water')
        root.moves['Water Pulse'] = pokemon_ddl.Move('Water Pulse', 60, 1.0, 'Spec', 'Water')
        root.moves['Water Spout'] = pokemon_ddl.Move('Water Spout', 150, 1.0, 'Spec', 'Water')
        root.moves['Whirlpool'] = pokemon_ddl.Move('Whirlpool', 15, 0.7, 'Spec', 'Water')

        # Bug-type moves
        root.moves['Bug Buzz'] = pokemon_ddl.Move('Bug Buzz', 90, 1.0, 'Spec', 'Bug')
        root.moves['Signal Beam'] = pokemon_ddl.Move('Signal Beam', 75, 1.0, 'Spec', 'Bug')
        root.moves['Silver Wind'] = pokemon_ddl.Move('Silver Wind', 60, 1.0, 'Spec', 'Bug')

        # Electric-type moves
        root.moves['Charge Beam'] = pokemon_ddl.Move('Charge Beam', 50, 0.9, 'Spec', 'Electric')
        root.moves['Discharge'] = pokemon_ddl.Move('Discharge', 80, 1.0, 'Spec', 'Electric')
        root.moves['Shock Wave'] = pokemon_ddl.Move('Shock Wave', 60, 1.0, 'Spec', 'Electric')
        root.moves['Thunder'] = pokemon_ddl.Move('Thunder', 120, 0.7, 'Spec', 'Electric')
        root.moves['Thunderbolt'] = pokemon_ddl.Move('Thunderbolt', 95, 1.0, 'Spec', 'Electric')
        root.moves['Thundershock'] = pokemon_ddl.Move('Thundershock', 40, 1.0, 'Spec', 'Electric')
        root.moves['Zap Cannon'] = pokemon_ddl.Move('Zap Cannon', 120, 0.5, 'Spec', 'Electric')

        # Psychic-type moves
        root.moves['Confusion'] = pokemon_ddl.Move('Confusion', 50, 1.0, 'Spec', 'Psychic')
        root.moves['Dream Eater'] = pokemon_ddl.Move('Dream Eater', 100, 1.0, 'Spec', 'Psychic')
        root.moves['Extrasensory'] = pokemon_ddl.Move('Extrasensory', 80, 1.0, 'Spec', 'Psychic')
        root.moves['Future Sight'] = pokemon_ddl.Move('Future Sight', 80, 0.9, 'Spec', 'Psychic')
        root.moves['Luster Purge'] = pokemon_ddl.Move('Luster Purge', 70, 1.0, 'Spec', 'Psychic')
        root.moves['Mirror Coat'] = pokemon_ddl.Move('Mirror Coat', 0, 1.0, 'Spec', 'Psychic')
        root.moves['Mist Ball'] = pokemon_ddl.Move('Mist Ball', 70, 1.0, 'Spec', 'Psychic')
        root.moves['Psybeam'] = pokemon_ddl.Move('Psybeam', 65, 1.0, 'Spec', 'Psychic')
        root.moves['Psychic'] = pokemon_ddl.Move('Psychic', 90, 1.0, 'Spec', 'Psychic')
        root.moves['Psycho Boost'] = pokemon_ddl.Move('Psycho Boost', 140, 0.9, 'Spec', 'Psychic')
        root.moves['Psywave'] = pokemon_ddl.Move('Psywave', 0, 0.8, 'Spec', 'Psychic')

        # Dark-type moves
        root.moves['Dark Pulse'] = pokemon_ddl.Move('Dark Pulse', 80, 1.0, 'Spec', 'Dark')

        # Steel-type moves
        root.moves['Doom Desire'] = pokemon_ddl.Move('Doom Desire', 120, 0.85, 'Spec', 'Steel')
        root.moves['Flash Cannon'] = pokemon_ddl.Move('Flash Cannon', 80, 1.0, 'Spec', 'Steel')
        root.moves['Mirror Shot'] = pokemon_ddl.Move('Mirror Shot', 65, 0.85, 'Spec', 'Steel')

        # Dragon-type moves
        root.moves['Draco Meteor'] = pokemon_ddl.Move('Draco Meteor', 140, 0.9, 'Spec', 'Dragon')
        root.moves['Dragon Pulse'] = pokemon_ddl.Move('Dragon Pulse', 90, 1.0, 'Spec', 'Dragon')
        root.moves['Dragon Rage'] = pokemon_ddl.Move('Dragon Rage', 0, 1.0, 'Spec', 'Dragon')
        root.moves['Dragonbreath'] = pokemon_ddl.Move('Dragonbreath', 60, 1.0, 'Spec', 'Dragon')
        root.moves['Roar of Time'] = pokemon_ddl.Move('Roar of Time', 150, 0.9, 'Spec', 'Dragon')
        root.moves['Spacial Rend'] = pokemon_ddl.Move('Spacial Rend', 100, 0.95, 'Spec', 'Dragon')
        root.moves['Twister'] = pokemon_ddl.Move('Twister', 40, 1.0, 'Spec', 'Dragon')

        # Ground-type moves
        root.moves['Earth Power'] = pokemon_ddl.Move('Earth Power', 90, 1.0, 'Spec', 'Ground')
        root.moves['Mud Bomb'] = pokemon_ddl.Move('Mud Bomb', 65, 0.85, 'Spec', 'Ground')
        root.moves['Mud Shot'] = pokemon_ddl.Move('Mud Shot', 55, 0.95, 'Spec', 'Ground')
        root.moves['Mud-slap'] = pokemon_ddl.Move('Mud-slap', 20, 1.0, 'Spec', 'Ground')

        # Fire-type moves
        root.moves['Blast Burn'] = pokemon_ddl.Move('Blast Burn', 150, 0.9, 'Spec', 'Fire')
        root.moves['Ember'] = pokemon_ddl.Move('Ember', 40, 1.0, 'Spec', 'Fire')
        root.moves['Eruption'] = pokemon_ddl.Move('Eruption', 150, 1.0, 'Spec', 'Fire')
        root.moves['Fire Blast'] = pokemon_ddl.Move('Fire Blast', 120, 0.85, 'Spec', 'Fire')
        root.moves['Fire Spin'] = pokemon_ddl.Move('Fire Spin', 15, 0.7, 'Spec', 'Fire')
        root.moves['Flamethrower'] = pokemon_ddl.Move('Flamethrower', 95, 1.0, 'Spec', 'Fire')
        root.moves['Heat Wave'] = pokemon_ddl.Move('Heat Wave', 100, 0.9, 'Spec', 'Fire')
        root.moves['Lava Plume'] = pokemon_ddl.Move('Lava Plume', 80, 1.0, 'Spec', 'Fire')
        root.moves['Magma Storm'] = pokemon_ddl.Move('Magma Storm', 120, 0.7, 'Spec', 'Fire')
        root.moves['Overheat'] = pokemon_ddl.Move('Overheat', 140, 0.9, 'Spec', 'Fire')

        # Ghost-type moves
        root.moves['Night Shade'] = pokemon_ddl.Move('Night Shade', 0, 1.0, 'Spec', 'Ghost')
        root.moves['Ominous Wind'] = pokemon_ddl.Move('Ominous Wind', 60, 1.0, 'Spec', 'Ghost')
        root.moves['Shadow Ball'] = pokemon_ddl.Move('Shadow Ball', 80, 1.0, 'Spec', 'Ghost')

        # Normal-type moves
        root.moves['Hidden Power'] = pokemon_ddl.Move('Hidden Power', 0, 1.0, 'Spec', 'Normal')
        root.moves['Hyper Beam'] = pokemon_ddl.Move('Hyper Beam', 150, 0.9, 'Spec', 'Normal')
        root.moves['Hyper Voice'] = pokemon_ddl.Move('Hyper Voice', 90, 1.0, 'Spec', 'Normal')
        root.moves['Judgment'] = pokemon_ddl.Move('Judgment', 100, 1.0, 'Spec', 'Normal')
        root.moves['Snore'] = pokemon_ddl.Move('Snore', 40, 1.0, 'Spec', 'Normal')
        root.moves['SonicBoom'] = pokemon_ddl.Move('SonicBoom', 0, 0.9, 'Spec', 'Normal')
        root.moves['Spit Up'] = pokemon_ddl.Move('Spit Up', 0, 1.0, 'Spec', 'Normal')
        root.moves['Swift'] = pokemon_ddl.Move('Swift', 60, 1.0, 'Spec', 'Normal')
        root.moves['Tri Attack'] = pokemon_ddl.Move('Tri Attack', 80, 1.0, 'Spec', 'Normal')
        root.moves['Trump Card'] = pokemon_ddl.Move('Trump Card', 0, 1.0, 'Spec', 'Normal')
        root.moves['Uproar'] = pokemon_ddl.Move('Uproar', 50, 1.0, 'Spec', 'Normal')
        root.moves['Weather Ball'] = pokemon_ddl.Move('Weather Ball', 50, 1.0, 'Spec', 'Normal')
        root.moves['Wring Out'] = pokemon_ddl.Move('Wring Out', 0, 1.0, 'Spec', 'Normal')

    if 'Status Move':
        # Normal-type moves
        root.moves['Acupressure'] = pokemon_ddl.Move('Acupressure', 0, 1.0, 'Stat', 'Normal')
        root.moves['Assist'] = pokemon_ddl.Move('Assist', 0, 1.0, 'Stat', 'Normal')
        root.moves['Attract'] = pokemon_ddl.Move('Attract', 0, 1.0, 'Stat', 'Normal')
        root.moves['Baton Pass'] = pokemon_ddl.Move('Baton Pass', 0, 1.0, 'Stat', 'Normal')
        root.moves['Belly Drum'] = pokemon_ddl.Move('Belly Drum', 0, 1.0, 'Stat', 'Normal')
        root.moves['Block'] = pokemon_ddl.Move('Block', 0, 1.0, 'Stat', 'Normal')
        root.moves['Camouflage'] = pokemon_ddl.Move('Camouflage', 0, 1.0, 'Stat', 'Normal')
        root.moves['Captivate'] = pokemon_ddl.Move('Captivate', 0, 1.0, 'Stat', 'Normal')
        root.moves['Charm'] = pokemon_ddl.Move('Charm', 0, 1.0, 'Stat', 'Normal')
        root.moves['Conversion'] = pokemon_ddl.Move('Conversion', 0, 1.0, 'Stat', 'Normal')
        root.moves['Conversion 2'] = pokemon_ddl.Move('Conversion 2', 0, 1.0, 'Stat', 'Normal')
        root.moves['Copycat'] = pokemon_ddl.Move('Copycat', 0, 1.0, 'Stat', 'Normal')
        root.moves['Defense Curl'] = pokemon_ddl.Move('Defense Curl', 0, 1.0, 'Stat', 'Normal')
        root.moves['Disable'] = pokemon_ddl.Move('Disable', 0, 0.8, 'Stat', 'Normal')
        root.moves['Double Team'] = pokemon_ddl.Move('Double Team', 0, 1.0, 'Stat', 'Normal')
        root.moves['Encore'] = pokemon_ddl.Move('Encore', 0, 1.0, 'Stat', 'Normal')
        root.moves['Endure'] = pokemon_ddl.Move('Endure', 0, 1.0, 'Stat', 'Normal')
        root.moves['Flash'] = pokemon_ddl.Move('Flash', 0, 1.0, 'Stat', 'Normal')
        root.moves['Focus Energy'] = pokemon_ddl.Move('Focus Energy', 0, 1.0, 'Stat', 'Normal')
        root.moves['Follow Me'] = pokemon_ddl.Move('Follow Me', 0, 1.0, 'Stat', 'Normal')
        root.moves['Foresight'] = pokemon_ddl.Move('Foresight', 0, 1.0, 'Stat', 'Normal')
        root.moves['Glare'] = pokemon_ddl.Move('Glare', 0, 0.75, 'Stat', 'Normal')
        root.moves['Growl'] = pokemon_ddl.Move('Growl', 0, 1.0, 'Stat', 'Normal')
        root.moves['Growth'] = pokemon_ddl.Move('Growth', 0, 1.0, 'Stat', 'Normal')
        root.moves['Harden'] = pokemon_ddl.Move('Harden', 0, 1.0, 'Stat', 'Normal')
        root.moves['Heal Bell'] = pokemon_ddl.Move('Heal Bell', 0, 1.0, 'Stat', 'Normal')
        root.moves['Helping Hand'] = pokemon_ddl.Move('Helping Hand', 0, 1.0, 'Stat', 'Normal')
        root.moves['Howl'] = pokemon_ddl.Move('Howl', 0, 1.0, 'Stat', 'Normal')
        root.moves['Leer'] = pokemon_ddl.Move('Leer', 0, 1.0, 'Stat', 'Normal')
        root.moves['Lock-on'] = pokemon_ddl.Move('Lock-on', 0, 1.0, 'Stat', 'Normal')
        root.moves['Lovely Kiss'] = pokemon_ddl.Move('Lovely Kiss', 0, 0.75, 'Stat', 'Normal')
        root.moves['Lucky Chant'] = pokemon_ddl.Move('Lucky Chant', 0, 1.0, 'Stat', 'Normal')
        root.moves['Me First'] = pokemon_ddl.Move('Me First', 0, 1.0, 'Stat', 'Normal')
        root.moves['Mean Look'] = pokemon_ddl.Move('Mean Look', 0, 1.0, 'Stat', 'Normal')
        root.moves['Metronome'] = pokemon_ddl.Move('Metronome', 0, 1.0, 'Stat', 'Normal')
        root.moves['Milk Drink'] = pokemon_ddl.Move('Milk Drink', 0, 1.0, 'Stat', 'Normal')
        root.moves['Mimic'] = pokemon_ddl.Move('Mimic', 0, 1.0, 'Stat', 'Normal')
        root.moves['Mind Reader'] = pokemon_ddl.Move('Mind Reader', 0, 1.0, 'Stat', 'Normal')
        root.moves['Minimize'] = pokemon_ddl.Move('Minimize', 0, 1.0, 'Stat', 'Normal')
        root.moves['Moonlight'] = pokemon_ddl.Move('Moonlight', 0, 1.0, 'Stat', 'Normal')
        root.moves['Morning Sun'] = pokemon_ddl.Move('Morning Sun', 0, 1.0, 'Stat', 'Normal')
        root.moves['Nature Power'] = pokemon_ddl.Move('Nature Power', 0, 1.0, 'Stat', 'Normal')
        root.moves['Odor Sleuth'] = pokemon_ddl.Move('Odor Sleuth', 0, 1.0, 'Stat', 'Normal')
        root.moves['Pain Split'] = pokemon_ddl.Move('Pain Split', 0, 1.0, 'Stat', 'Normal')
        root.moves['Perish Song'] = pokemon_ddl.Move('Perish Song', 0, 1.0, 'Stat', 'Normal')
        root.moves['Protect'] = pokemon_ddl.Move('Protect', 0, 1.0, 'Stat', 'Normal')
        root.moves['Psych Up'] = pokemon_ddl.Move('Psych Up', 0, 1.0, 'Stat', 'Normal')
        root.moves['Recover'] = pokemon_ddl.Move('Recover', 0, 1.0, 'Stat', 'Normal')
        root.moves['Recycle'] = pokemon_ddl.Move('Recycle', 0, 1.0, 'Stat', 'Normal')
        root.moves['Refresh'] = pokemon_ddl.Move('Refresh', 0, 1.0, 'Stat', 'Normal')
        root.moves['Roar'] = pokemon_ddl.Move('Roar', 0, 1.0, 'Stat', 'Normal')
        root.moves['Safeguard'] = pokemon_ddl.Move('Safeguard', 0, 1.0, 'Stat', 'Normal')
        root.moves['Scary Face'] = pokemon_ddl.Move('Scary Face', 0, 0.9, 'Stat', 'Normal')
        root.moves['Screech'] = pokemon_ddl.Move('Screech', 0, 0.85, 'Stat', 'Normal')
        root.moves['Sharpen'] = pokemon_ddl.Move('Sharpen', 0, 1.0, 'Stat', 'Normal')
        root.moves['Sing'] = pokemon_ddl.Move('Sing', 0, 0.55, 'Stat', 'Normal')
        root.moves['Sketch'] = pokemon_ddl.Move('Sketch', 0, 1.0, 'Stat', 'Normal')
        root.moves['Slack Off'] = pokemon_ddl.Move('Slack Off', 0, 1.0, 'Stat', 'Normal')
        root.moves['Sleep Talk'] = pokemon_ddl.Move('Sleep Talk', 0, 1.0, 'Stat', 'Normal')
        root.moves['Smokescreen'] = pokemon_ddl.Move('Smokescreen', 0, 1.0, 'Stat', 'Normal')
        root.moves['Softboiled'] = pokemon_ddl.Move('Softboiled', 0, 1.0, 'Stat', 'Normal')
        root.moves['Splash'] = pokemon_ddl.Move('Splash', 0, 1.0, 'Stat', 'Normal')
        root.moves['Stockpile'] = pokemon_ddl.Move('Stockpile', 0, 1.0, 'Stat', 'Normal')
        root.moves['Substitute'] = pokemon_ddl.Move('Substitute', 0, 1.0, 'Stat', 'Normal')
        root.moves['Supersonic'] = pokemon_ddl.Move('Supersonic', 0, 0.55, 'Stat', 'Normal')
        root.moves['Swagger'] = pokemon_ddl.Move('Swagger', 0, 0.9, 'Stat', 'Normal')
        root.moves['Swallow'] = pokemon_ddl.Move('Swallow', 0, 1.0, 'Stat', 'Normal')
        root.moves['Sweet Kiss'] = pokemon_ddl.Move('Sweet Kiss', 0, 0.75, 'Stat', 'Normal')
        root.moves['Sweet Scent'] = pokemon_ddl.Move('Sweet Scent', 0, 1.0, 'Stat', 'Normal')
        root.moves['Swords Dance'] = pokemon_ddl.Move('Swords Dance', 0, 1.0, 'Stat', 'Normal')
        root.moves['Tail Whip'] = pokemon_ddl.Move('Tail Whip', 0, 1.0, 'Stat', 'Normal')
        root.moves['Teeter Dance'] = pokemon_ddl.Move('Teeter Dance', 0, 1.0, 'Stat', 'Normal')
        root.moves['Tickle'] = pokemon_ddl.Move('Tickle', 0, 1.0, 'Stat', 'Normal')
        root.moves['Transform'] = pokemon_ddl.Move('Transform', 0, 1.0, 'Stat', 'Normal')
        root.moves['Whirlwind'] = pokemon_ddl.Move('Whirlwind', 0, 1.0, 'Stat', 'Normal')
        root.moves['Wish'] = pokemon_ddl.Move('Wish', 0, 1.0, 'Stat', 'Normal')
        root.moves['Yawn'] = pokemon_ddl.Move('Yawn', 0, 1.0, 'Stat', 'Normal')

        # Psychic-type moves
        root.moves['Agility'] = pokemon_ddl.Move('Agility', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Amnesia'] = pokemon_ddl.Move('Amnesia', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Barrier'] = pokemon_ddl.Move('Barrier', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Calm Mind'] = pokemon_ddl.Move('Calm Mind', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Cosmic Power'] = pokemon_ddl.Move('Cosmic Power', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Gravity'] = pokemon_ddl.Move('Gravity', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Guard Swap'] = pokemon_ddl.Move('Guard Swap', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Heal Block'] = pokemon_ddl.Move('Heal Block', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Healing Wish'] = pokemon_ddl.Move('Healing Wish', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Heart Swap'] = pokemon_ddl.Move('Heart Swap', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Hypnosis'] = pokemon_ddl.Move('Hypnosis', 0, 0.7, 'Stat', 'Psychic')
        root.moves['Imprison'] = pokemon_ddl.Move('Imprison', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Kinesis'] = pokemon_ddl.Move('Kinesis', 0, 0.8, 'Stat', 'Psychic')
        root.moves['Light Screen'] = pokemon_ddl.Move('Light Screen', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Lunar Dance'] = pokemon_ddl.Move('Lunar Dance', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Magic Coat'] = pokemon_ddl.Move('Magic Coat', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Meditate'] = pokemon_ddl.Move('Meditate', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Miracle Eye'] = pokemon_ddl.Move('Miracle Eye', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Power Swap'] = pokemon_ddl.Move('Power Swap', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Power Trick'] = pokemon_ddl.Move('Power Trick', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Psycho Shift'] = pokemon_ddl.Move('Psycho Shift', 0, 0.9, 'Stat', 'Psychic')
        root.moves['Reflect'] = pokemon_ddl.Move('Reflect', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Rest'] = pokemon_ddl.Move('Rest', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Role Play'] = pokemon_ddl.Move('Role Play', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Skill Swap'] = pokemon_ddl.Move('Skill Swap', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Teleport'] = pokemon_ddl.Move('Teleport', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Trick'] = pokemon_ddl.Move('Trick', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Trick Room'] = pokemon_ddl.Move('Trick Room', 0, 1.0, 'Stat', 'Psychic')

        # Poison-type moves
        root.moves['Acid Armor'] = pokemon_ddl.Move('Acid Armor', 0, 1.0, 'Stat', 'Poison')
        root.moves['Gastro Acid'] = pokemon_ddl.Move('Gastro Acid', 0, 1.0, 'Stat', 'Poison')
        root.moves['Poison Gas'] = pokemon_ddl.Move('Poison Gas', 0, 0.55, 'Stat', 'Poison')
        root.moves['Poisonpowder'] = pokemon_ddl.Move('Poisonpowder', 0, 0.75, 'Stat', 'Poison')
        root.moves['Toxic'] = pokemon_ddl.Move('Toxic', 0, 0.85, 'Stat', 'Poison')
        root.moves['Toxic Spikes'] = pokemon_ddl.Move('Toxic Spikes', 0, 1.0, 'Stat', 'Poison')

        # Grass-type moves
        root.moves['Aromatherapy'] = pokemon_ddl.Move('Aromatherapy', 0, 1.0, 'Stat', 'Grass')
        root.moves['Cotton Spore'] = pokemon_ddl.Move('Cotton Spore', 0, 0.85, 'Stat', 'Grass')
        root.moves['Grasswhistle'] = pokemon_ddl.Move('Grasswhistle', 0, 0.55, 'Stat', 'Grass')
        root.moves['Ingrain'] = pokemon_ddl.Move('Ingrain', 0, 1.0, 'Stat', 'Grass')
        root.moves['Leech Seed'] = pokemon_ddl.Move('Leech Seed', 0, 0.9, 'Stat', 'Grass')
        root.moves['Sleep Powder'] = pokemon_ddl.Move('Sleep Powder', 0, 0.75, 'Stat', 'Grass')
        root.moves['Spore'] = pokemon_ddl.Move('Spore', 0, 1.0, 'Stat', 'Grass')
        root.moves['Stun Spore'] = pokemon_ddl.Move('Stun Spore', 0, 0.75, 'Stat', 'Grass')
        root.moves['Synthesis'] = pokemon_ddl.Move('Synthesis', 0, 1.0, 'Stat', 'Grass')
        root.moves['Worry Seed'] = pokemon_ddl.Move('Worry Seed', 0, 1.0, 'Stat', 'Grass')

        # Water-type moves
        root.moves['Aqua Ring'] = pokemon_ddl.Move('Aqua Ring', 0, 1.0, 'Stat', 'Water')
        root.moves['Rain Dance'] = pokemon_ddl.Move('Rain Dance', 0, 1.0, 'Stat', 'Water')
        root.moves['Water Sport'] = pokemon_ddl.Move('Water Sport', 0, 1.0, 'Stat', 'Water')
        root.moves['Withdraw'] = pokemon_ddl.Move('Withdraw', 0, 1.0, 'Stat', 'Water')

        # Ghost-type moves
        root.moves['Confuse Ray'] = pokemon_ddl.Move('Confuse Ray', 0, 1.0, 'Stat', 'Ghost')
        root.moves['Curse'] = pokemon_ddl.Move('Curse', 0, 1.0, 'Stat', 'Ghost')
        root.moves['Destiny Bond'] = pokemon_ddl.Move('Destiny Bond', 0, 1.0, 'Stat', 'Ghost')
        root.moves['Grudge'] = pokemon_ddl.Move('Grudge', 0, 1.0, 'Stat', 'Ghost')
        root.moves['Nightmare'] = pokemon_ddl.Move('Nightmare', 0, 1.0, 'Stat', 'Ghost')
        root.moves['Spite'] = pokemon_ddl.Move('Spite', 0, 1.0, 'Stat', 'Ghost')

        # Dark-type moves
        root.moves['Dark Void'] = pokemon_ddl.Move('Dark Void', 0, 0.8, 'Stat', 'Dark')
        root.moves['Embargo'] = pokemon_ddl.Move('Embargo', 0, 1.0, 'Stat', 'Dark')
        root.moves['Fake Tears'] = pokemon_ddl.Move('Fake Tears', 0, 1.0, 'Stat', 'Dark')
        root.moves['Flatter'] = pokemon_ddl.Move('Flatter', 0, 1.0, 'Stat', 'Dark')
        root.moves['Memento'] = pokemon_ddl.Move('Memento', 0, 1.0, 'Stat', 'Dark')
        root.moves['Nasty Plot'] = pokemon_ddl.Move('Nasty Plot', 0, 1.0, 'Stat', 'Dark')
        root.moves['Snatch'] = pokemon_ddl.Move('Snatch', 0, 1.0, 'Stat', 'Dark')
        root.moves['Switcheroo'] = pokemon_ddl.Move('Switcheroo', 0, 1.0, 'Stat', 'Dark')
        root.moves['Taunt'] = pokemon_ddl.Move('Taunt', 0, 1.0, 'Stat', 'Dark')
        root.moves['Torment'] = pokemon_ddl.Move('Torment', 0, 1.0, 'Stat', 'Dark')

        # Bug-type moves
        root.moves['Defend Order'] = pokemon_ddl.Move('Defend Order', 0, 1.0, 'Stat', 'Bug')
        root.moves['Heal Order'] = pokemon_ddl.Move('Heal Order', 0, 1.0, 'Stat', 'Bug')
        root.moves['Spider Web'] = pokemon_ddl.Move('Spider Web', 0, 1.0, 'Stat', 'Bug')
        root.moves['String Shot'] = pokemon_ddl.Move('String Shot', 0, 0.95, 'Stat', 'Bug')
        root.moves['Tail Glow'] = pokemon_ddl.Move('Tail Glow', 0, 1.0, 'Stat', 'Bug')

        # Fighting-type moves
        root.moves['Bulk Up'] = pokemon_ddl.Move('Bulk Up', 0, 1.0, 'Stat', 'Fighting')
        root.moves['Detect'] = pokemon_ddl.Move('Detect', 0, 1.0, 'Stat', 'Fighting')

        # Electric-type moves
        root.moves['Charge'] = pokemon_ddl.Move('Charge', 0, 1.0, 'Stat', 'Electric')
        root.moves['Magnet Rise'] = pokemon_ddl.Move('Magnet Rise', 0, 1.0, 'Stat', 'Electric')
        root.moves['Thunder Wave'] = pokemon_ddl.Move('Thunder Wave', 0, 1.0, 'Stat', 'Electric')

        # Flying-type moves
        root.moves['Defog'] = pokemon_ddl.Move('Defog', 0, 1.0, 'Stat', 'Flying')
        root.moves['Featherdance'] = pokemon_ddl.Move('Featherdance', 0, 1.0, 'Stat', 'Flying')
        root.moves['Mirror Move'] = pokemon_ddl.Move('Mirror Move', 0, 1.0, 'Stat', 'Flying')
        root.moves['Roost'] = pokemon_ddl.Move('Roost', 0, 1.0, 'Stat', 'Flying')
        root.moves['Tailwind'] = pokemon_ddl.Move('Tailwind', 0, 1.0, 'Stat', 'Flying')

        # Dragon-type moves
        root.moves['Dragon Dance'] = pokemon_ddl.Move('Dragon Dance', 0, 1.0, 'Stat', 'Dragon')

        # Ice-type moves
        root.moves['Hail'] = pokemon_ddl.Move('Hail', 0, 1.0, 'Stat', 'Ice')
        root.moves['Haze'] = pokemon_ddl.Move('Haze', 0, 1.0, 'Stat', 'Ice')
        root.moves['Mist'] = pokemon_ddl.Move('Mist', 0, 1.0, 'Stat', 'Ice')

        # Steel-type moves
        root.moves['Iron Defense'] = pokemon_ddl.Move('Iron Defense', 0, 1.0, 'Stat', 'Steel')
        root.moves['Metal Sound'] = pokemon_ddl.Move('Metal Sound', 0, 0.85, 'Stat', 'Steel')

        # Ground-type moves
        root.moves['Mud Sport'] = pokemon_ddl.Move('Mud Sport', 0, 1.0, 'Stat', 'Ground')
        root.moves['Sand-attack'] = pokemon_ddl.Move('Sand-attack', 0, 1.0, 'Stat', 'Ground')
        root.moves['Spikes'] = pokemon_ddl.Move('Spikes', 0, 1.0, 'Stat', 'Ground')

        # Rock-type moves
        root.moves['Rock Polish'] = pokemon_ddl.Move('Rock Polish', 0, 1.0, 'Stat', 'Rock')
        root.moves['Sandstorm'] = pokemon_ddl.Move('Sandstorm', 0, 1.0, 'Stat', 'Rock')
        root.moves['Stealth Rock'] = pokemon_ddl.Move('Stealth Rock', 0, 1.0, 'Stat', 'Rock')

        # Fire-type moves
        root.moves['Sunny Day'] = pokemon_ddl.Move('Sunny Day', 0, 1.0, 'Stat', 'Fire')
        root.moves['Will-o-wisp'] = pokemon_ddl.Move('Will-o-wisp', 0, 0.75, 'Stat', 'Fire')

    for move_id, move in root.moves.items():
        if move.category == 'Stat':
            print(move.toString())



if __name__ == '__main__':
    runDML()
