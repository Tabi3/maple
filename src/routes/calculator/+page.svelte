<script>
	import Accordion from '../../components/Accordion.svelte';
</script>

<div class="card">
	<h1>Wolfram Alpha <i class="bx bxs-calculator" /></h1>
	<form action="" id="Query-Wolfram" class="flex items-center justify-center">
		<input type="text" placeholder="2*x" class="rounded-lg w-full h-full p-2" />
		<button type="button" value="Submit" class="bx bxs-send hov-btn h-full aspect-square p-4" />
	</form>

	<div class="dark-box flex flex-col gap-4">
		<p>PLOTS</p>
		<div class="flex flex-col bg-inherit gap-4 plots">
			<img
				src="https://cdn.discordapp.com/attachments/813982140559523861/1050352564857745478/image.png"
				alt=""
			/>
		</div>
	</div>
</div>
<div class="results card">
	<h1>Results</h1>
	<div class="flex flex-col gap-4 overflow-visible !bg-transparent">
		<Accordion caption="Result">
			2 x
		</Accordion>
		<Accordion caption="Geometric figure">
			Line
		</Accordion>
		<Accordion caption="Properties as a real function">
			<div class="dark-box col-span-2">
				<table>
					<thead>
						<tr>
							<td>Domain</td>
							<td>Range</td>
							<td>Bijectivity</td>
							<td>Parity</td>
						</tr>
					</thead>
					<tr>
						<td>R (all real numbers)</td>
						<td>R (all real numbers)</td>
						<td>Bijective </td>
						<td>Odd</td>
					</tr>
				</table>
			</div>
		</Accordion>
		<Accordion caption="Derivative">
			d/dx(x×2) = 2
		</Accordion>
		<Accordion caption="Integral">
			integral2 x dx = x^2 + constant
		</Accordion>
	</div>
</div>

<style>
	input {
		border: 1px #111 solid;
	}
	.plots img {
		border-radius: 0.5rem;
	}
</style>
