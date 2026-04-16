# Versi Setelah Perbaikan
class CheckoutService:
    MEMBERSHIP_DISCOUNT_RATE = 0.1

    def process_checkout(self, user, item, quantity):
        self._validate_stock(item.stock, quantity)
        
        final_price = self._calculate_total_price(user, item.price, quantity)
        
        self._save_transaction(user.id, item.id, quantity, final_price)
        self._send_confirmation_notification(user.email)
        
        return final_price

    def _calculate_total_price(self, user, price, quantity):
        total = price * quantity
        if user.is_member:
            total -= total * self.MEMBERSHIP_DISCOUNT_RATE
        return total

    def _validate_stock(self, available_stock, requested_quantity):
        if available_stock < requested_quantity:
            raise ValueError("Insufficient stock for this item.")