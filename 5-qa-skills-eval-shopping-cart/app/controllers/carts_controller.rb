class CartsController < ApplicationController

  before_action :authenticate_user!

  def show
    @cart = current_user.cart
    @line_items = @cart.line_items
    @products = Product.all
  end

  def add_item
    @cart = current_user.cart
    @product = Product.find(params[:product_id])
    @line_item = LineItem.new(cart: @cart, product: @product, quantity: 1)

    if @line_item.save
      @product.update(inventory: @product.inventory - 1)
      respond_to do |format|
        format.js {render :layout => false}
        format.html {redirect_to cart_path}
      end
    else 
      flash[:error] = "There was an error adding the item to your cart"
    end
  end

  def remove_item
    @line_item = LineItem.find(params[:id])
    @product = @line_item.product
    if @line_item.destroy
      @product.update(inventory: @product.inventory + 1)
      respond_to do |format|
        format.js {render :layout => false}
      end
    else 
      flash[:error] = "There was an error removing the item from your cart"
    end
    
  end

  private

  def authenticate_user!
    redirect_to new_user_session_path unless user_signed_in?  
  end
  
end
