<script lang="ts">
	import '../app.css';
	import { onMount } from 'svelte';
	export let data: any;
	let docm: Document;
	let body: HTMLElement | null;
	let acc: HTMLElement | null;
	let hls: HTMLElement | null;
	let hbj: HTMLElement | null;
	let hvd: HTMLCollectionOf<HTMLElement | Element>;
	let hvr: Array<string>;

	let cookies = (doc: Document) => {
		return document.cookie.split('; ').reduce((prev: { [key: string]: any }, current) => {
			const [name, ...value]: string | string[] = current.split('=');
			prev[name] = value.join('=');
			return prev;
		}, {});
	};
	let darkmode = () => {
		body?.classList.toggle('dark');
		body?.classList.toggle('bg-[#111]');
		body?.classList.toggle('text-white');
		docm.cookie = 'darkmode=false;';
		if (body?.classList.contains('dark')) docm.cookie = 'darkmode=true;';
	};
	let exphls = () => {
		hls?.classList.toggle('expanded');
		acc?.classList.remove('expanded');
	};
	let expacc = () => {
		acc?.classList.toggle('expanded');
		hls?.classList.remove('expanded');
	};
	onMount(() => {
		docm = document;
		body = document.querySelector('body');
		acc = document.getElementById('acc');
		hls = document.getElementById('hls');
		hbj = document.getElementById('hovered-obj');
		hvd = document.getElementsByClassName('ho');
		hvr = ['Account', 'Toggle Dark Mode', 'Hyperlinks'];
		Array.from(hvd).forEach((a: HTMLElement | Element, b: number) => {
			if (a instanceof HTMLElement) {
				a.onmouseover = () => {
					if (hbj != undefined) {
						hbj.innerHTML = hvr[b];
						hbj.classList.toggle('opacity-0');
					}
				};
				a.onmouseleave = () => {
					if (hbj != undefined) {
						hbj.classList.toggle('opacity-0');
					}
				};
			}
		});
		document.cookie = data.cookies;
		if (cookies(docm).darkmode === 'true') {
			darkmode();
		}
		console.log(cookies(docm));
	});
</script>

<svelte:body class="duration-100" />
<nav>
	<div class="nav-content">
		<button class="bx bxs-user p-3 widget ho" on:click={expacc} />
		<button class="bx bxs-moon p-3 widget ho" on:click={darkmode} />
		<button class="bx bxs-dashboard p-3 widget ho" on:click={exphls} />
		<p id="hovered-obj" class="opacity-0"/>

		<form action="">
			<input type="text" placeholder="search" />
			<button class="bx bxs-search" />
		</form>
	</div>
</nav>
<div class="dropdowns">
	<div class="dropdown-shells">
		<div class="closed flex-wrap" id="hls">
			<a href="/" class="gr-ul aspect-square"><i class="bx bxs-home-alt-2" /></a>
			<a href="/school" class="gr-ul aspect-square"><i class="bx bxs-graduation" /></a>
			<a href="/calculator" class="gr-ul aspect-square"><i class="bx bx-math" /></a>
			<a href="/maple-bot" class="gr-ul aspect-square"><i class="bx bxs-leaf" /></a>
		</div>
		<div class="closed flex-col" id="acc">
			<a href="/" class="gr-ul"><i class="bx bxs-home-alt-2" /> Home</a>
			<a href="/" class="gr-ul"><i class="bx bxs-graduation" /> Khub</a>
			<a href="/" class="gr-ul"><i class="bx bx-math" /> Wolfram Alpha</a>
		</div>
	</div>
</div>

<slot />
<footer>
	<div class="footer-contents">
		<div class="!bg-inherit">
			This is the footer. If you're at the school tab then you may see it bugged. this is because
			the body element is still too short
		</div>
		<div class="!bg-inherit">
			This part of the footer will contain hyperlinks to companies / sponsors. This can also display
			the site description, vision or mission.
		</div>
	</div>
</footer>
