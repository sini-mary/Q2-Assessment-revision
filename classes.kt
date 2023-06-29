// 1.**Ancestral Stories:** In many African cultures, the art of storytelling is passed
// down from generation to generation. Imagine you're creating an application that records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.



fun main() {




    val recipes = Recipe(   arrayOf("Rice", "Spices"), "one hour",
        "fry the meat till golden under low heat", "proteins and energy")
    val ethiopianRecipe = EthiopianRecipe("grounded wheat", arrayOf("Wheat", "brown wheat"),
        " am maximum of three days",
        "ferment the flour the fry it under low heat for two minute",
        "energy"
    )
    ethiopianRecipe.ethiopiansSpecial()



   val recipes = Recipe(   arrayOf("Rice", "Spices"), "one hour",
       "fry the meat till golden under low heat", "proteins and energy")
   val ethiopianRecipe = EthiopianRecipe("grounded wheat", arrayOf("Wheat", "brown wheat"),
       " am maximum of three days",
       "ferment the flour the fry it under low heat for two minute",
       "energy"
   )
   ethiopianRecipe.ethiopiansSpecial()




 
 
 }
 
 
 
 
 open class Recipe(var ingredients: Array<String>, var preparationTime: String, val cookingMethod: String, var nutritionalValue: String) {
 
 
    fun getIngredients() {

        println("The ingredients is $ingredients")

 
 
    }
 fun checkallergerns(){
    if (allergens == null)
    allergens=arrayOf<String>(){
    else{
        print(allergens[0])
        }
 }


    fun getPreparationTime() {
        var preptime=10
      if(preptime<=10){
        println("It is an easy meal to prepare")
      }
      else{
        println("The meal will take a longe period to prepare")
      }

      

 
 
    }
 
 
 
    fun servingportions(var guests:Int){
        var foodcapacity =100
        var foodserved = 0
        if(guests <= foodcapacity){
            foodserved = guests
            }else{
                foodserved = foodcapacity



        }
       
    }
       fun portions(preferredServing: Int): String {
       return when {
           preferredServing > serving -> {
               val portionAmount = (preferredServing / serving)
               "The portion of ingredients can be increased $portionAmount times"
           }
                   preferredServing < serving -> {
               val portionAmount = (serving / preferredServing)
               "The portion of ingredients can be decreased $portionAmount times"
           }
           else ->{
               "The portion of food serves $serving"
           }
       }
   }
 
 }
 
 
 class MorrocanRecipe(var specialIngredient: String, ingredients: Array<String>, preparationTime: String, cookingMethod: String,
    
 nutritionalValue: String) : Recipe(ingredients, preparationTime, cookingMethod, nutritionalValue) {
    fun specialRecipe() {
        println("The special recipe of Morocco is $specialIngredient")
 
 
    }
 
 
 }
 
 
 
 
 class EthiopianRecipe(var specialIngredient: String, ingredients: Array<String>, preparationTime: String, cookingMethod: String,
    nutritionalValue: String) : Recipe(ingredients, preparationTime, cookingMethod, nutritionalValue) {
 
 
    fun ethiopiansSpecial() {
        println("The special recipe of Ethiopia is $specialIngredient")
 
 
 
 
    }
 
 
 }
 
 
 class NigerianRecipe(var specialIngredient: String, ingredients: Array<String>, preparationTime: String, cookingMethod: String,
    nutritionalValue: String) : Recipe(ingredients, preparationTime, cookingMethod, nutritionalValue) {
 
 
    fun nigerianSpecial() {
        println("The special recipe of Nigeria is $specialIngredient ")
       
    }
 }





 //
// 2. **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// Methods.


class MorrocanRecipe(var specialIngredient: String, ingredients: Array<String>, preparationTime: String, cookingMethod: String,
   
nutritionalValue: String) : Recipe(ingredients, preparationTime, cookingMethod, nutritionalValue) {
   fun specialRecipe() {
       println("The special recipe of Morocco is $specialIngredient")


   }


}




class EthiopianRecipe(var specialIngredient: String, ingredients: Array<String>, preparationTime: String, cookingMethod: String,
   nutritionalValue: String) : Recipe(ingredients, preparationTime, cookingMethod, nutritionalValue) {


   fun ethiopiansSpecial() {
       println("The special recipe of Ethiopia is $specialIngredient")




   }


}


class NigerianRecipe(var specialIngredient: String, ingredients: Array<String>, preparationTime: String, cookingMethod: String,
   nutritionalValue: String) : Recipe(ingredients, preparationTime, cookingMethod, nutritionalValue) {


   fun nigerianSpecial() {
       println("The special recipe of Nigeria is $specialIngredient ")
      
   }
}


// 3. **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to
// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// These classes might relate to each other through inheritance.

fun main() {
    val animal1 = Predator("Leopard", "meat", "30yrs", "East to West", "spot and stalk")
    println(animal1.speciesInfo())
    val animal2 = Prey("Antelope", "grass", "20yrs", "seasonal", "lying flat on ground")
    println(animal2.speciesInfo())
   val animal3=Animal("Lion","Meat","50yrs","West
    to East","Roar")
 
 
 
 
 }
 
 
 
 
 open class Species(val name: String, val diet: String, val lifespan: String, val migrationPatterns: String) {
   open fun speciesInfo(): String {
        return "$name feeds on $diet, it has a lifespan of $lifespan and migrates $migrationPatterns"
    }
 }
 class Predator(name: String, diet: String, lifespan: String, migrationPatterns: String, val huntingMethod: String) : Species(name, diet, lifespan, migrationPatterns) {
    override fun speciesInfo(): String {
        return super.speciesInfo()
    }
    
 }
 
 
 class Prey(name: String, diet: String, lifespan: String, migrationPatterns: String, val defenseMechanism: String) : Species(name, diet, lifespan, migrationPatterns) {
    override fun speciesInfo(): String {
        return super.speciesInfo()
    }

