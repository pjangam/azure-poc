namespace ShoppingCart.Controllers
{
    public class Money
    {
        public decimal Amount { get; set; }
        public string Currency { get; set; }

        public Money()
        {
            
        }
        public Money(string currency,decimal amount)
        {
            Currency = currency;
            Amount = amount;
        }
    }
}