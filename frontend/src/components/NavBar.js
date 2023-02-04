import Style from "./NavBar.module.scss";

function NavBar() {
  return (
    <nav className={Style.nav}>
      <a href="/" className={Style.site_title}>
        Site name
      </a>
      <ul>
        <li className={Style.active}>
          <a href="/Register">Sign up</a>
        </li>
        <li>
          <a href="/About">About</a>
        </li>
      </ul>
    </nav>
  );
}

export default NavBar;
