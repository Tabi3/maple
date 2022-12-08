<script lang="ts">
</script>

<div class="banner">
	<div class="banner-inner-formatter">
		<div class="banner-content-shell">
			<div class="banner-content">
				<h1>
					Cloudbound <i class="bx bxs-cloud" />
				</h1>
				<p>Data Bounded to the Clouds</p>
			</div>
		</div>
		<div class="banner-other-content">
			<a href="./CS-works" class="hov-btn hover:!bg-[rgba(0,0,0,0.5)]">Link to Framework Stuff</a>
			<ul class="banner-others">
				<li class=""><i class="bx bxs-home-alt-2" /></li>
				<li class=""><i class="bx bxs-graduation" /></li>
				<li class=""><i class="bx bx-math" /></li>
			</ul>
		</div>
	</div>
</div>
<div class="main-container">
	<main class="grid grid-cols-2 gap-8">
		<div class="card col-span-2 intro">
			<h1>Brief overview</h1>
			<p>
				Remember Maple? Yeah, the website design looked bad after a while. It was due to very poor
				designing coming from my part. However, I have grown, therefore Cloud Bound changes that.
			</p>
			<p>Cloudbound also offers new features such as:</p>
		</div>
		<section
			class="bleed"
			style="--sprite: url('/src/images/Spritesheet.png'); 
				   --bg-image: url('/src/images/background-banner.jpg')"
		>
			<div class="card">
				<div class="sprite-container">
					<sprite class="sprite-1" />
				</div>
				<div class="text-shell">
					<p>Widgets for School</p>
				</div>
			</div>
			<div class="card">
				<div class="sprite-container">
					<sprite class="sprite-2" />
				</div>
				<div class="text-shell">
					<p>Cloud Storage</p>
				</div>
			</div>
			<div class="card">
				<div class="sprite-container">
					<sprite class="sprite-3" />
				</div>
				<div class="text-shell">
					<p>Accounts</p>
				</div>
			</div>
		</section>
		<div class="card">
			<h1>Cloudbound Features</h1>
			<p>
				Cloudbound is a cloud computing platform, meaning you can do calculations and store data
				here to use on another device.
			</p>
			<p>Features include:</p>
			<ul>
				<li>Reskinning Websites</li>
				<li>Calendar</li>
				<li>School Tools (PSHS exclusive)</li>
			</ul>
		</div>
		<div class="services">
			<h1>Services I used</h1>
			<div class="flex h-full overflow-visible"
			 	style="--sprite: url('src/images/Spritesheet.png')">
				<button class="hov-btn">
					<sprite class="Wolfram-sprite"/>
					<div>Wolfram Alpha</div>
				</button>
				<button class="hov-btn">
					<sprite class="Khub-sprite"/>
					<div>PSHS KHUB</div>
				</button>
				<button class="hov-btn">
					<sprite class="Maple-sprite"/>
					<div>Maple Bot</div>
				</button>
			</div>
		</div>
		<div class="page-text">
			<h1>Hello Teacher! Again...</h1>
			<p>
				Again Temporary text... But I guess it's okay because I managed to use sprites here even
				though I just needed html elements for them. I also did an overhaul as you can see because
				the site looks very different. I also made the website more compatible with 720p displays by
				solving some padding stuff and limiting the entire website's width to be 1280px. Also you
				may have noticed I added a css folder. This is because the css is very long and needs to be
				put on another file.
			</p>
		</div>
		<div class="card">
			<h1>Computer-Science Notes</h1>
			<ul>
				<li>99% of the wesite has not been implemented</li>
				<li>The navbar has the account widget but it shows the hyperlinks instead</li>
				<li>Only one hyperlink works at the moment and that is <i class="bx bxs-graduation" /></li>
				<li>The search bar is useless</li>
			</ul>
		</div>
		<div class="dark-box col-span-2">
			<table>
				<thead>
					<tr>
						<td>Column 1</td>
						<td>Column 2</td>
					</tr>
				</thead>
				<tr>
					<td>This is a Table</td>
					<td>It is pretty neet</td>
				</tr>
				<tr>
					<td>However they're hard to deal with</td>
					<td>This is why grids are superior</td>
				</tr>
				<tr>
					<td>But Tables existed before grids</td>
					<td>So many websites rely on tables</td>
				</tr>
			</table>
		</div>
	</main>
</div>

<style>
	.banner-others::after {
		background-image: none;
	}
	.services .hov-btn {
		position: relative;
		width: 100%;
		text-align: center;
	}
	.services .hov-btn div {
		position: absolute;
		background-color: transparent;
		bottom: 0;
		left: 0;
		padding: 1rem;
	}
	.services .hov-btn sprite {
		position: absolute;
		transition: all 200ms;
		object-fit: cover;
		opacity: 0;
		top: 0;
		left: 0;
	}
	.services .hov-btn:hover div {
		color: #ef4648 !important;
	}
	.services .hov-btn:hover sprite {
		opacity: 1;
		filter: blur(2px);
	}
	.services {
		overflow: visible;
		gap: 2rem;
		display: flex;
		flex-direction: column;
	}
	.services h1 {
		font-size: 2rem;
	}
	.intro {
		text-align: center;
		padding: 6.75% 12.5%;
	}
	.sprite-1 {
		background: var(--sprite) -732px 0;
		width: 136px;
		height: 88px;
	}
	.sprite-2 {
		background: var(--sprite) -869px -44px;
		width: 40px;
		height: 40px;
	}
	.sprite-3 {
		background: var(--sprite) -869px -3px;
		width: 40px;
		height: 40px;
	}
	.Khub-sprite {
		background: var(--sprite) 0 0;
		width: 474px;
		height: 1080px;
	}
	.Wolfram-sprite {
		background: var(--sprite) -475px -426px;
		background-position-x: -800px;
		width: 877px;
		height: 1080px;
	}
	.Maple-sprite {
		background: var(--sprite) -475px 0px;
		width: 256px;
		height: 426px;
	}
</style>
