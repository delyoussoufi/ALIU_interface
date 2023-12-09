import { Component } from '@angular/core';

@Component({
  selector: 'app-parent-search-info',
  templateUrl: './parent-search-info.component.html',
  styleUrls: ['./parent-search-info.component.css']
})
export class ParentSearchInfoComponent {
  isInfoVisible = true;

  onSearchPerformed(): void {
    this.isInfoVisible = false;
  }
}


