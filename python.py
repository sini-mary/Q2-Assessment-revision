class Stories:
   def __init__(self,title,moral_value,length,language):
       self.title=title
       self.moral_value=moral_value
       self.length=length
       self.language=language


   def getStory(self):
       return f"The story {self.title}  teaches a moral of {self.moral_value}  is of length {self.length}.The language used in this story is {self.language}" 


story= Stories ("Born A crime","Do not give up",12,"English")
print(story.getStory())




class StoryTeller:
   def __init__(self,name,language, title):
       self.name =name
       self.title=title
       self.language=language
   def tellStories(self):
       return f"{self.name} is telling {self.title} in {self.language}"


stories=StoryTeller("Grace Ogot","Luo","Tekayo")
print(stories.tellStories()) 


class Translator(StoryTeller):
   def __init__(self,targetLanguage,name, title,language):
       self.name=name
       self.title=title
       self.language=language
       self.targetLanguage=targetLanguage


   def tellStory(self):
       return f"{self.name} translates {self.title} from {self.language} to {self.targetLanguage}" 


translate=Translator("Luo" ,"Paula Karimi","Tekayo","Kiswahili") 
print(translate.tellStory())       
# question2
class Recipe:
   
    def __init__(self,name,country,unique_ingredients,preparation_time,cooking_method,nutritional_value) :
       
        self.name=name
        self.country=country
        self.unique_ingredients=unique_ingredients
        self.preparation_time=preparation_time
        self.cooking_method=cooking_method
        self.nutritional_value=nutritional_value


class MoroccanRecipe(Recipe):


   def __init__(self, name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value):


       super().__init__(name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value)




   def cook(self):
      
       return f"For {self.name} in {self.country}  cook the meal with {self.unique_ingredients} for {self.preparation_time} by {self.cooking_method} to gain  more {self.nutritional_value}"
  




class EthopianRecipe(Recipe):
   def __init__(self, name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value):
    super().__init__(name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value)
   def cook(self):


       return f"For {self.name} in {self.country}  cook the meal with {self.unique_ingredients} for {self.preparation_time} by {self.cooking_method} to gain  more {self.nutritional_value}"
  




class  NigerianRecipe(Recipe):


   def __init__(self, name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value):


       super().__init__(name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value)


   def cook(self):


       return f"For {self.name} in {self.country}  cook the meal with {self.unique_ingredients} for {self.preparation_time} by {self.cooking_method} to gain  more {self.nutritional_value}"
  
moroccan= MoroccanRecipe("Wheat","Morocco","vinegar","30 minutes","grilling","cumin")


ethiopian= EthopianRecipe("chicken_breasts","Ethiopia","white wine","45 minutes","stewing","doro wat")


nigerian=NigerianRecipe("Jollof","Nigeria","pepper","3 hours","stirring","proteins")


print(nigerian.cook())
print(moroccan.cook())
print(ethiopian.cook())
# question3
class Species:
   def __init__(self, name, diet, lifespan, migration_patterns):
       self.name = name
       self.diet = diet
       self.lifespan = lifespan
       self.migration_patterns = migration_patterns
   def species_info(self):
       return (f"{self.name} feeds on{self.diet}, it has a lifespan of {self.lifespan} and migrates {self.migration_patterns}")
class Predator (Species):
   def __init__(self, name, diet, lifespan, migration_patterns, hunting_method):
       super().__init__(name, diet, lifespan, migration_patterns)
       self.hunting_method = hunting_method
   def species_info(self):
       return super().species_info()
animal1 = Predator("Leopard", "meat", "30yrs", "East to West", "spot and stalk")
print(animal1.species_info())
class Prey(Species):
   def __init__(self, name, diet, lifespan, migration_patterns, defense_mechanism):
       super().__init__(name, diet, lifespan, migration_patterns)
       self.defense_mechanism = defense_mechanism
   def species_info(self):
       return super().species_info()
animal2 = Prey("Antellope", "grass", "20yrs", "seasonal", "lying flat on ground")
print(animal2.species_info())


# 4.**African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or stages.



class Artist:
   def __init__(self, name, country, music_type, instruments):
       self.name = name
       self.country = country
       self.music_type = music_type
       self.instruments = instruments
   def artist_detail(self):
       print(f"name: {self.name}, country: {self.country}, musicType: {self.music_type}, instruments: {', '.join(self.instruments)}")
class Performance(Artist):
   def __init__(self, name, country, music_type, instruments, stage_time):
       super().__init__(name, country, music_type, instruments)
       self.stage_time = stage_time
   def scheduling(self):
       print(f"name: {self.name}, musicType: {self.music_type}, time: {self.stage_time}")
   def play_instrument(self, instrument):
        
          print(f"{self.name} is not playing {instrument}")
       if instrument in self.instruments:
           print(f"{self.name} is playing {instrument}")
       else:
           print(f"{self.name} is not playing {instrument}")
class Stage(Artist):
   def __init__(self, name, country, music_type, instruments, capacity, location):
       super().__init__(name, country, music_type, instruments)
       self.capacity = capacity
       self.location = location
   def performance(self):
       print(f"name: {self.name}, country: {self.country}, musicType: {self.music_type}, capacity: {self.capacity}, place: {self.location}")
artist = Artist("jayz", "Canada", "hiphop", instruments=["guitar", "piano"])
artist.artist_detail()
perform = Performance("sautisol", "Kenya", "bongo", instruments=["guitar", "piano"], stage_time="2 hours")
perform.scheduling()
perform.play_instrument("guitar")
stage = Stage("Bridget blue", "Kenya", "gospel", instruments=["piano", "harp", "violin"], capacity=100, location="Nakuru")
stage.performance()

print("The festival lineup is:")
for performance in [performance1, performance2, performance3]:
   print(performance.festival_lineup.__dict__)
# Print the schedule
print("\nThe schedule is:")
for performance in [performance1, performance2, performance3]:
   print(performance.schedule)
# Print the stages
print("The stages are:")
for stage in [stage1, stage2]:
   print(stage.stage_arrangements)




class Product:
def __init__(self,name,price,quantity) :
self.name=name
self.price=price
self.quantity=quantity
def getTotalValue(self):
return (float)(self.price*self.quantity)


product1=Product("Mango",20,22)
print(product1.getTotalValue())   





