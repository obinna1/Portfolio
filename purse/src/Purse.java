//converstion: 1 pound = 240 pence, 1 shilling = 12 pence(for me to undersand) what im looking at 3

//this is the purse class that will be used to create the purse objects
public class Purse {
    private int pounds; 
    private double pence;
    private double shillings;
    
    // constructor 

    public void purse2(int pounds, double shillings, double pence) {
        //this is the constructor that will be used to create the purse objects
        this.pounds = pounds;
        this.shillings = shillings;
        this.pence = pence;
    }
    
    // getters
    //gets the pounds
    public int getPounds() {
        return pounds;
    }
    //getts the shillings
    public double getShillings() {
        return shillings;
    }
    //gets the pence
    public double getPence() {
        return pence;
    }
    
    // add the money 
    public void addPounds(int pounds) {
        this.pounds += pounds;
    }
    
    public void addShillings(double shillings) {
        double totalShillings = this.shillings + shillings;
        // if the total shillings is greater than or equal to 20 what happens next 


        if (totalShillings >= 20) {
            int extraPounds = (int) (totalShillings / 20); // get the extra pounds
            // add the extra pounds to the current pounds
            this.pounds += extraPounds;
            // get the remainder of the shillings
            totalShillings %= 20;
        }
        
        // set the remaning shillings to the total shillings
        this.shillings = totalShillings;
    }
    // add the pence
    public void addPence(double pence) {
        double totalPence = this.pence + pence;
        // if the total pence is greater than or equal to 12
        if (totalPence >= 12) {
            int extraShillings = (int) (totalPence / 12); // get the extra shillings
            // add the extra shillings to the current shillings
            this.shillings += extraShillings;
            // get the remainder of the pence
            totalPence %= 12;
        }
        // set the remaning pence to the total pence
        this.pence = totalPence;
    }
    
    // spend money 
    public void spend(int poundsToRemove, int shillingsToRemove, int penceToRemove) {
        // get the total pence to remove
        int totalPence = (int) (poundsToRemove * 240 + shillingsToRemove * 12 + penceToRemove);
        // get the current pence
        int currentPence = (int) (pounds * 240 + shillings * 12 + pence);
        // remove the total pence from the current pence
        currentPence -= totalPence;
        // if the current pence is less than 0
        if (currentPence < 0) {
            // print insufficient funds
            System.out.println("Insufficient funds!");
        
            return;
        }
        // set the pounds to the current pence divided by 240
        pounds = currentPence / 240;
        currentPence %= 240;
        shillings = currentPence / 12;
        pence = currentPence % 12;
    }
    
    // print the Amount of money in the purse
    public String toString() {
        return "Pounds: " + pounds + " Shillings: " + shillings + " Pence: " + pence;
    }
}
