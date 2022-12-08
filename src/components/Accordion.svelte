<script lang="ts">
	export let caption: string | String;
	let expanded: boolean = false;
	let expand = (params: any) => (expanded = !expanded);
</script>

<div class="accordion h-fit flex flex-col overflow-visible w-full ">
	<button
		class="caption p-4 pastel-line-y relative overflow-hidden w-full shadow-md rounded-md"
		on:click={expand}
	>
		<p class="text-left">{caption}</p>
	</button>
	<div class="card {!expanded ? 'hidden-res' : ''} result mt-4">
		<slot />
	</div>
</div>

<style>
	.result {
		transition: all 200ms;
	}
	.hidden-res {
		margin: 0;
		height: 0;
		padding: 0;
	}
</style>
