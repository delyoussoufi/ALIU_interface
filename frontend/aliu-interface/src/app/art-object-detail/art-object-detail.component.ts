import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ArtDataService } from '../art-data.service';

@Component({
  selector: 'app-art-object-detail',
  templateUrl: './art-object-detail.component.html',
  styleUrls: ['./art-object-detail.component.css']
})
export class ArtObjectDetailComponent implements OnInit {
  artObject: any;
  ownerships: any[] = [];
  artObjectId: string = '';
  timelineEvents: any[] = [];
  
  constructor(
    private route: ActivatedRoute,
    private artDataService: ArtDataService
  ) { }

  ngOnInit(): void {
    this.artObjectId = this.route.snapshot.paramMap.get('id')!;
    this.fetchArtObjectDetails();
  }

  fetchArtObjectDetails(): void {
    // Fetch art object details
    this.artDataService.getArtObjectById(this.artObjectId).subscribe(
      data => {
        this.artObject = data;
      },
      error => {
        console.error('There was an error fetching the art object details!', error);
      }
    );

    // Fetch ownerships
    this.artDataService.getOwnerships(this.artObjectId).subscribe(
      data => {
        this.ownerships = data;
        this.prepareTimeline(data);
      },
      error => {
        console.error('There was an error fetching ownerships!', error);
      }
    );

  }

  prepareTimeline(ownerships: any[]): void {

  // Sort the ownerships array by the OwnershipFrom date
  ownerships.sort((a, b) => {
    let dateA = a.OwnershipFrom ? new Date(a.OwnershipFrom).getTime() : new Date(0).getTime(); // Convert to timestamp
    let dateB = b.OwnershipFrom ? new Date(b.OwnershipFrom).getTime() : new Date(0).getTime(); // Convert to timestamp
    return dateA - dateB;
  });

  // Then map the sorted array to timelineEvents
  this.timelineEvents = ownerships.map(ownership => {
    // Extract year and month using string manipulation
    let formattedOwnershipFrom = ownership.OwnershipFrom ? ownership.OwnershipFrom.substring(0, 7) : 'Unknown start date';
    let formattedOwnershipUntil = ownership.OwnershipUntil ? ownership.OwnershipUntil.substring(0, 7) : 'Unknown end date';

    return {
      ownerName: ownership.OwnerName,
      period: `From ${formattedOwnershipFrom} to ${formattedOwnershipUntil}`,
      description: ownership.OwnerDescription || 'Ownership Detail',
    };
  });
}
      

  objectKeys(obj: any): string[] {
    return Object.keys(obj);
  }

  formatKey(key: string): string {
    // Format the key for display
    return key.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase());
  }

}
