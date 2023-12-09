import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent {
  searchTerm: string = '';

  constructor(private router: Router) { }

  searchArtObjects(): void {
    if (this.searchTerm) {
      this.router.navigate(['/art-objects'], { queryParams: { query: this.searchTerm } });
    }
  }
}
