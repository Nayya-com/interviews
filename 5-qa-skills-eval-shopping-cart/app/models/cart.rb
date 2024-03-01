class Cart < ApplicationRecord
  belongs_to :user
  has_many :line_items, dependent: :destroy

  def subtotal
    line_items.map(&:product).map(&:price).sum
  end
end
