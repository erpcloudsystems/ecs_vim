frappe.pages['kitchen-screen'].on_page_load = function(wrapper) {
	 new MyPage(wrapper)
}

MyPage = Class.extend({
	init: function (wrapper){
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
			title: 'Kitchen Order',
			single_column: true
		});


		this.make(name)
		
	},
	make: async function(name){

		let me = this.page;

		id = undefined
		let body = frappe.test_app_page.body
		let model = frappe.test_app_page.model

		await $(frappe.render_template(body,this)).appendTo(this.page.main)
		await $(frappe.render_template(model,this)).appendTo(this.page.main)
		generateOrderCards();

	}
});


const body = `
<div class="container">
<div class="row">

</div>
<div class="row" id="orderGrid">
	<!-- Orders will be dynamically added here -->
</div>
</div>

`
function markAsCompleted(orderId) {
	// Here you can implement the logic to mark the order as completed.
	// For this example, we will simply hide the card representing the order.
	const button = document.querySelector(`button[data-order="${orderId}"]`);
	const card = button.closest('.card');
	if (card) {
		card.style.display = "none";
	}
}

const orders = [
	{ id: 123, table: 5, items: ['Pasta', 'Pizza', 'Salad'] },
	{ id: 124, table: 8, items: ['Burger', 'Fries', 'Coke'] },
	{ id: 124, table: 8, items: ['Burger', 'Fries', 'Coke'] },
	{ id: 124, table: 8, items: ['Burger', 'Fries', 'Coke'] },
	{ id: 124, table: 8, items: ['Burger', 'Fries', 'Coke'] },
	{ id: 124, table: 8, items: ['Burger', 'Fries', 'Coke'] },
	{ id: 124, table: 8, items: ['Burger', 'Fries', 'Coke'] },
	{ id: 124, table: 8, items: ['Burger', 'Fries', 'Coke'] },
	{ id: 124, table: 8, items: ['Burger', 'Fries', 'Coke'] },
	{ id: 124, table: 8, items: ['Burger', 'Fries', 'Coke'] },
	{ id: 124, table: 8, items: ['Burger', 'Fries', 'Coke'] },
	{ id: 124, table: 8, items: ['Burger', 'Fries', 'Coke'] },
	{ id: 124, table: 8, items: ['Burger', 'Fries', 'Coke'] },
	{ id: 124, table: 8, items: ['Burger', 'Fries', 'Coke'] },
	// Add more orders as needed
];

// Function to generate order cards dynamically
function generateOrderCards() {
	const orderGrid = document.getElementById('orderGrid');

	orders.forEach((order) => {
		const card = document.createElement('div');
		card.classList.add('col-md-4');
		card.innerHTML = `
			<div class="card">
				<div class="card-header">
					Order #${order.id}
				</div>
				<div class="card-body">
					<h5 class="card-title">Table ${order.table}</h5>
					<p class="card-text">Items:</p>
					<ul>
						${order.items.map(item => `<li>${item}</li>`).join('')}
					</ul>
					<button class="btn btn-success" data-order="${order.id}" onclick="markAsCompleted(${order.id})">Mark as Completed</button>
				</div>
			</div>
		`;

		orderGrid.appendChild(card);
	});
}

// Initial generation of order cards

model =`
<div class="modal fade bd-example-modal-lg" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <img id="select-img">
    </div>
  </div>
</div>
` 
frappe.test_app_page = {
	body:body,
	model: model
}

