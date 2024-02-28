# This file should ensure the existence of records required to run the application in every environment (production,
# development, test). The code here should be idempotent so that it can be executed at any point in every environment.
# The data can then be loaded with the bin/rails db:seed command (or created alongside the database with db:setup).
#
# Example:
#
#   ["Action", "Comedy", "Drama", "Horror"].each do |genre_name|
#     MovieGenre.find_or_create_by!(name: genre_name)
#   end

User.find_or_create_by!(email: "qa@nayya.com") do |user|
  user.password = "nayya123"
end 

User.find_or_create_by!(email: "qa2@nayya.com") do |user|
  user.password = "nayya123"
end 

Product.find_or_create_by!(name: "Health Insurance Gold") do |product|  
  product.price = 1000
  product.inventory = 10
end

Product.find_or_create_by!(name: "Health Insurance Silver") do |product|  
  product.price = 100
  product.inventory = 10
end

Product.find_or_create_by!(name: "Health Insurance Bronze") do |product|  
  product.price = 100
  product.inventory = 10
end
